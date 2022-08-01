# -*- coding: utf-8 -*-

import random
from myqt import mkQApp
import datetime
import os
from protocolwindow import ProtocolWindow
from protocol_eeg_slides_2022 import *
from path_stimuli import *

########################
######## PARAMS ########
########################



params_RD_protocole = {

'freq_confort' : 0.21, # CHANGER SELON LA FREQ CONFORT DU SUJET
'freq_lent' : 0.1,
'freq_rapide' : 0.5,

'duree_entrainement_absolute_evaluation' : 15,
'duration_absolute_evaluation' : 30,
'duration_absolute_evaluation_other_stim' : 5,
'duration_absolute_evaluation_rest' : 30,

'duration_freeresp' : 30,

'duree_presentation' : 20,
'duree_entrainement' : 40,
'duree_blocs' : 300,
'duree_repos' : 15,
'duree_entrainement_repos' : 10

}

params_RD_debug = {

'freq_confort' : .25,
'freq_lent' : .1,
'freq_rapide' : 0.5,

'duree_entrainement_absolute_evaluation' : 1,
'duration_absolute_evaluation' : 3,
'duration_absolute_evaluation_other_stim' : 1,
'duration_absolute_evaluation_rest' : 1,

'duration_freeresp' : 10,

'duree_presentation' : 1,
'duree_entrainement' : 1,
'duree_blocs' : 3,
'duree_repos' : 1,
'duree_entrainement_repos' : 1

}


########################
######## RANDOM ########
########################

#### odor presentation
odor_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odor_num_random = odor_num.copy()
random.shuffle(odor_num_random)

#### odor presentation
image_num = 10

#### odor presentation
sound_num = 10

#### session presentation
all_session = ['lent', 'lent', 'lent', 'rapide', 'rapide', 'rapide', 'confort', 'confort', 'confort']
all_session_random = all_session.copy()
random.shuffle(all_session_random)





################################
######## SLIDE GESTION ######## 
################################


def generate_ea_txt(i):
        
    ea_txt = f"""
    <div class="center container ">
            <p style="font-size:50pt">Prenez l'odeur n°{odor_num_random[i]}</p>
    </div>

    <div class="instruction">
            <p style="font-size:20pt">Appuyez sur ESPACE</p> 
            <p style="font-size:20pt">pour commencer</p>
    </div>
    
    """

    return ea_txt



def generate_random_picture(already_selected):

	path_source = os.getcwd()

	os.chdir(path_images)

	list_pic = os.listdir()
	list_pic.remove('RespiExp_Nez.png')
	list_pic.remove('RespiExp_Bouche.png')

	if len(already_selected) != 0:
		[list_pic.remove(file_i) for file_i in already_selected]

	file_selected = list_pic[random.randint(0, len(list_pic)-1)]

	already_selected.append(file_selected)

	txt_to_print = f"""
	<div class="center container ">
			<p><img src="{path_images}/{file_selected}" height=960 ></p>
	</div>   
	"""

	os.chdir(path_source)

	return txt_to_print, already_selected




def random_sound(already_selected):

	path_source = os.getcwd()

	os.chdir(path_soundfile)

	list_sound = [file_i for file_i in os.listdir() if file_i.find('_full') == -1]

	if len(already_selected) != 0:
		[list_sound.remove(file_i) for file_i in already_selected]

	file_selected = list_sound[random.randint(0, len(list_sound)-1)]

	already_selected.append(file_selected)

	random_file = os.path.join(path_soundfile, file_selected)

	os.chdir(path_source)

	return random_file, already_selected





########################
######## BLOCKS ########
########################

mode_respi_driver = None # just for debug

params_RD_used = params_RD_debug

block_entrainement_ea = [   

        {'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt1},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt2},
        {'type': 'display', 'duration': params_RD_used['duree_entrainement_absolute_evaluation'], 'text' : style+entrainement_txt3},
        {'type': 'display', 'duration': params_RD_used['duree_entrainement_absolute_evaluation'], 'text' : style+entrainement_txt4},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt5},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt6},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt7},
]


block_ea = [
        
        {'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt1},

        # boucle
        {'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(0)},
        {'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3},
        {'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_rest'], 'text' : style+ea_txt4},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5},
        #fin boucle

        {'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt6}

]

block_start_exp = [

        {'type': 'display', 'duration': 'wait_key', 'text' : style+start_exp_txt1},

]

block_présentation = [

        {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt1},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1},
        {'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}},    
        {'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt2},

]

block_entrainement = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt4},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':100},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_entrainement'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':101},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':102},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':103},
    {'type': 'display', 'duration': params_RD_used['duree_entrainement_repos'], 'text' : style+session_txt5, 'trigger':104},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger':105},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt3},

]

block_FR_CV = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt1, 'trigger':60},
    {'type': 'display', 'duration': params_RD_used['duration_freeresp'], 'text' : style+freeresp_txt2, 'trigger':61},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':63},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt3, 'trigger':62},

]
        
block_15 = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':12},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':13},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :15},

]

block_confort = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':30},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':31},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':32},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':33},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :34},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :35},

]

block_50 = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':50},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':51},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':52},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':53},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :54},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :55},

]



################################
######## PROTOCOLES ########
################################



def select_session_freq(protocole, cond, params_RD_used):

    if cond == 'lent':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':10})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':11})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':12})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':13})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :14})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :15})

    if cond == 'confort':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':30})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':31})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':32})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':33})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :34})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :35})

    if cond == 'rapide':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':50})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':51})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':52})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':53})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :54})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :55})



def get_protocole_absolute_evaluation(params_RD_used):

	protocole_absolute_evaluation = []

	#### 1st part
	for i, _ in enumerate(odor_num_random):

		if i == 0:

			#### debut
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+debut_txt1})

			#### entrainement
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt1})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt2})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duree_entrainement'], 'text' : style+entrainement_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duree_entrainement_repos'], 'text' : style+entrainement_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt5})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt6})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt7})

			#### debut ea
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt1})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})

		elif i == len(odor_num_random)-1:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})

			#### end 1st part
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt6})

		else:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})

	#### 2nd part
	for i in range(image_num):

		if i == 0:

			#### initiate file selection
			already_selected = []

			#### debut
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+debut_ie_txt1})

			#### entrainement
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt1})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt2})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_ie_txt3})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_ie_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt5})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt2})

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt6})

			#### start part

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt7})

			#### debut esounda
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt2})
			random_image_i, already_selected = generate_random_picture(already_selected)
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+random_image_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_ie_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt5})

		elif i == image_num-1:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt2})
			random_image_i, already_selected = generate_random_picture(already_selected)
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+random_image_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_ie_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt5})

			#### end 2nd part
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt8})

		else:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt2})
			random_image_i, already_selected = generate_random_picture(already_selected)
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+random_image_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_ie_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_ie_txt5})

	#### 3nd part
	for i in range(sound_num):

		if i == 0:

			#### initiate file selection
			already_selected = []

			#### debut
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+debut_se_txt1})

			#### entrainement
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt1})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt2})
			random_sound_i, already_selected = random_sound(already_selected)
			protocole_absolute_evaluation.append({'type': 'son', 'sound_file' : random_sound_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_se_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt4})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt2})

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt5})
			
			#### reset file selection
			already_selected = []

			#### start part
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt6})

			#### debut ea
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt2})
			random_sound_i, already_selected = random_sound(already_selected)
			protocole_absolute_evaluation.append({'type': 'son', 'sound_file' : random_sound_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_se_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt4})

		elif i == sound_num-1:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt2})
			random_sound_i, already_selected = random_sound(already_selected)
			protocole_absolute_evaluation.append({'type': 'son', 'sound_file' : random_sound_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_se_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt4})

			#### end 3nd part
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt7})

		else:

			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt2})
			random_sound_i, already_selected = random_sound(already_selected)
			protocole_absolute_evaluation.append({'type': 'son', 'sound_file' : random_sound_i})
			protocole_absolute_evaluation.append({'type': 'question', 'question_list': question_list_other_stim})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation_other_stim'], 'text' : style+entrainement_se_txt3})
			protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_se_txt4})

	return protocole_absolute_evaluation






def get_protocol_session(mode_respi_driver, params_RD_used):

	protocole_session = []

	#### load respi protocol
	for i, cond in enumerate(all_session_random):
		
		if i == 0:

			#### block_start_exp

			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+start_exp_txt1})

			#### block_FR_CV

			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt1, 'trigger':60})
			protocole_session.append({'type': 'display', 'duration': params_RD_used['duration_freeresp'], 'text' : style+freeresp_txt2, 'trigger':61})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt3, 'trigger':62})
			protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':63})

			#### block_présentation

			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt1})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1})
			protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}})
			protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt2})

			#### block_entrainement
					
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt4})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':100})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
			protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_entrainement'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6., 'mode': mode_respi_driver}, 'trigger':101})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':102})
			protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':103})
			protocole_session.append({'type': 'display', 'duration': params_RD_used['duree_entrainement_repos'], 'text' : style+session_txt5, 'trigger':104})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger':105})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt3})

			#### session_RD

			select_session_freq(protocole_session, cond, params_RD_used)

		elif i == len(all_session_random)-1:

			#### session_RD

			select_session_freq(protocole_session, cond, params_RD_used)

			#### block_FR_CV
			
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt1, 'trigger':60})
			protocole_session.append({'type': 'display', 'duration': params_RD_used['duration_freeresp'], 'text' : style+freeresp_txt2, 'trigger':61})
			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt3, 'trigger':62})
			protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':63})

			#### fin_session

			protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_end_txt1})

		else:

			select_session_freq(protocole_session, cond, params_RD_used)
		
	return protocole_session



################################
######## START PROTOCOLE ########
################################


def start_protocolwindow(sujet, num_session, protocol, with_parallel=False, parallel_adress=None, with_serial=False, serial_port=None):

	log_name = f'sub{sujet}_ses0{num_session}_LogTrigger_{datetime.datetime.now()}.txt'
	log_name = log_name.replace(':', '-')

	#### write random order
	random_file = f'sub{sujet}_ses0{num_session}_bloc_random_order_{datetime.datetime.now()}.txt'
	random_file = random_file.replace(':', '-')

	random_file_txt = open(random_file,"w")
	random_file_txt.write(f'bloc randomization for session 0{num_session} : \n')
	for i in range(len(all_session_random)):
		random_file_txt.write(f'{all_session_random[i]} ')
	random_file_txt.close()

	if os.path.exists(log_name):
		os.remove(log_name)

	#### start protocolwindow
	app = mkQApp()
	if with_parallel:
			w = ProtocolWindow(protocol, log_name, with_parallel=with_parallel, parallel_adress=parallel_adress)
	elif with_serial:
			w = ProtocolWindow(protocol, log_name, with_serial=with_serial, serial_port=serial_port)
	else:
			w = ProtocolWindow(protocol, log_name, with_serial=with_serial, serial_port=serial_port)
	w.show()
	w.start()
	app.exec_()



if __name__ == '__main__':

	#### params
	# mode_respi_driver = 'line'
	mode_respi_driver = 'bouboul'

	# params_RD_used = params_RD_protocole
	params_RD_used = params_RD_debug

	#### protocol selection
	# protocol = get_protocol_session(mode_respi_driver, params_RD_used)
	protocol = get_protocole_absolute_evaluation(params_RD_used)

	#### sujet information
	sujet = '04'
	num_session = 3

	#### start
	start_protocolwindow(sujet, num_session, protocol, with_serial=False, serial_port=None)




