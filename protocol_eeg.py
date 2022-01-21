# -*- coding: utf-8 -*-

import random
from myqt import QT, mkQApp
import datetime
import os
from protocolwindow import ProtocolWindow, test_trigger_parralel
import time
from psychopy import parallel

########################
######## PARAMS ########
########################

params_RD_protocole = {

'duration_absolute_evaluation' : 30,
'duration_absolute_evaluation_rest' : 30,
'duree_entrainement_absolute_evaluation' : 40,

'freq_confort' : .218,
'freq_lent' : .15,
'freq_rapide' : .4,

'duration_freeresp' : 540,

'duree_presentation' : 20,
'duree_entrainement' : 40,
'duree_blocs' : 180,
'duree_repos' : 20,
'duree_entrainement_repos' : 10

}

params_RD_debug = {

'duration_absolute_evaluation' : 1,
'duration_absolute_evaluation_rest' : 1,
'duree_entrainement_absolute_evaluation' : 1,

'freq_confort' : .218,
'freq_lent' : .15,
'freq_rapide' : .4,

'duration_freeresp' : 1,

'duree_presentation' : 15,
'duree_entrainement' : 15,
'duree_blocs' : 30,
'duree_repos' : 10,
'duree_entrainement_repos' : 15

}

#### choose params
#params_RD_used = params_RD_protocole
params_RD_used = params_RD_debug



########################
######## RANDOM ########
########################

#### odor presentation
odor_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odor_num_random = odor_num.copy()
random.shuffle(odor_num_random)

#### session presentation
all_session = ['lent', 'lent', 'lent', 'rapide', 'rapide', 'rapide', 'confort', 'confort', 'confort']
all_session_random = all_session.copy()
random.shuffle(all_session_random)



########################
######## SLIDES ########
########################


style = """
<style>
.container {
    position: relative;
    color: black;
    margin: 0;
    height:100%;
}

.center {
    margin: 00;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.instruction {
    margin-top: 400%;
    margin-left: 0%;
}


</style>
"""


#### debut exp


debut_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de l'expérience</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

#### free resp


freeresp_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de respiration confort</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

freeresp_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Respiration Normale</p>
</div>

"""

freeresp_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Fin de respiration confort</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour continuer</p>
</div>
"""

#### entrainement

entrainement_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de l'évaluation des odeurs</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""


entrainement_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Prenez l'odeur n°1</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""


entrainement_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Evaluez l'odeur</p>
</div>
"""

entrainement_txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Posez l'odeur</p>
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

entrainement_txt5 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""

entrainement_txt6 = """
<div class="center container ">
        <p style="font-size:50pt">Prenez l'odeur n°2</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

entrainement_txt7 = """
<div class="center container ">
        <p style="font-size:50pt">Fin entrainement</p>
</div>
"""








#### évaluation absolue



ea_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Démarrer la première session d'évaluation</p>
</div>
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""


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





ea_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Evaluez l'odeur</p>
</div>
"""

ea_txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Posez l'odeur</p>
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

ea_txt5 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""



ea_txt6 = """
<div class="center container ">
        <p style="font-size:50pt">Fin première session</p>
</div>
"""



# session présentation

session_presentation_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de la présentation</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur espace lorsque vous</p>
        <p style="font-size:20pt">souhaitez démarrer</p>
</div>

"""

session_presentation_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Avez vous des questions ?</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur espace </p>
        <p style="font-size:20pt">pour continuer</p>
</div>

"""

session_presentation_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Session d’entrainement terminée</p>
        <p style="font-size:50pt">Avez vous des questions ?</p>
        <p style="font-size:50pt">Vous pouvez stopper l’expérience</p>
        <p style="font-size:50pt">lorsque vous le souhaitez</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer l’expérience</p>
</div>
"""

session_presentation_txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Session d’entrainement</p>

</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

# session repiration

start_exp_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Bienvenue dans cette session</p>
</div> 

<div class="instruction">      
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p> 
</div>
"""



session_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur ESPACE pour</p>
        <p style="font-size:50pt">démarrer une nouvelle session</p>
</div>
"""


session_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Respirez par le nez :</p>
        <p><img src="RespiExp_Nez.png" height=320 ></p>
</div>   

<div class="instruction">      
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour lancer le logiciel de respiration</p> 
</div>
"""


session_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Session terminée</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour passer à la suite</p>
</div>
"""

session_txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Veuillez remplir le questionnaire</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour passer à la suite</p>
</div>
"""

session_txt5 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

session_txt6 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""



#### fin session
session_end_txt1 ="""
<div class="center container ">
        <p style="font-size:50pt">Session terminée</p>
</div>

"""



################################
######## QUESTIONS ########
################################


question_list_STAI = [

    {'label': 'Je me sens calme', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Je me sens tendu(e), crispé(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Je me sens ému(e), bouleversé(e), contrarié(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Je suis décontracté(e), détendu(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Je suis satisfait(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Je suis inquiet, soucieux (inquiète, soucieuse)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},
    {'label': 'Quel niveau d’attention avez-vous porté a votre respiration ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Je suis relaxé(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complétement'},

]





########################
######## BLOCKS ########
########################



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
        {'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},    
        {'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt2},

]

block_entrainement = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt4},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':100},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_entrainement'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':101},
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
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':12},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':13},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :15},

]

block_confort = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':30},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':31},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':32},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':33},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :34},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :35},

]

block_50 = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':50},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2},
    {'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':51},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':52},
    {'type': 'question', 'question_list': question_list_STAI, 'trigger':53},
    {'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :54},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :55},

]



def select_session_freq(protocole, cond):

    if cond == 'lent':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':10})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':12})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':13})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :14})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :15})

    if cond == 'confort':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':30})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':31})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':32})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':33})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :34})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :35})

    if cond == 'rapide':

        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':50})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole.append({'type': 'respidriver', 'duration': params_RD_used['duree_blocs'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':51})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':52})
        protocole.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':53})
        protocole.append({'type': 'display', 'duration': params_RD_used['duree_blocs'], 'text' : style+session_txt5, 'trigger' :54})
        protocole.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger' :55})



################################
######## PROTOCOLES ########
################################


protocole_absolute_evaluation = []

for i in range(len(odor_num)):
    if i == 0:

        # debut
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+debut_txt1})

        # entrainement
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt1})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt2})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duree_entrainement'], 'text' : style+entrainement_txt3})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duree_entrainement_repos'], 'text' : style+entrainement_txt4})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt5})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt6})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+entrainement_txt7})

        # debut ea
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt1})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})

    elif i == len(odor_num)-1:

        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt6})

    else:

        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+generate_ea_txt(i)})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt3})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': params_RD_used['duration_absolute_evaluation'], 'text' : style+ea_txt4})
        protocole_absolute_evaluation.append({'type': 'display', 'duration': 'wait_key', 'text' : style+ea_txt5})


protocole_session = []

for i in range(len(all_session_random)):
    
    if i == 0:

        # block_start_exp

        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+start_exp_txt1})

        # block_freeresp

        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt1, 'trigger':60})
        protocole_session.append({'type': 'display', 'duration': params_RD_used['duration_freeresp'], 'text' : style+freeresp_txt2, 'trigger':61})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt3, 'trigger':62})
        protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':63})

        # block_présentation

        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt1})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1})
        protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_confort'], 'freq2': params_RD_used['freq_confort'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}})
        protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_presentation'], 'params' : {'freq1' : params_RD_used['freq_lent'], 'freq2': params_RD_used['freq_lent'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt2})

        # block_entrainement
                
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt4})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1, 'trigger':100})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt2})
        protocole_session.append({'type': 'respidriver', 'duration': params_RD_used['duree_entrainement'], 'params' : {'freq1' : params_RD_used['freq_rapide'], 'freq2': params_RD_used['freq_rapide'], 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':101})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt3, 'trigger':102})
        protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':103})
        protocole_session.append({'type': 'display', 'duration': params_RD_used['duree_entrainement_repos'], 'text' : style+session_txt5, 'trigger':104})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt6, 'trigger':105})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_txt1})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_presentation_txt3})

        # session_RD

        select_session_freq(protocole_session, all_session_random[i])

    elif i == len(all_session_random)-1:

        # session_RD

        select_session_freq(protocole_session, all_session_random[i])

        # block_FR_CV
        
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt1, 'trigger':60})
        protocole_session.append({'type': 'display', 'duration': params_RD_used['duration_freeresp'], 'text' : style+freeresp_txt2, 'trigger':61})
        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+freeresp_txt3, 'trigger':62})
        protocole_session.append({'type': 'question', 'question_list': question_list_STAI, 'trigger':63})


        # fin_session

        protocole_session.append({'type': 'display', 'duration': 'wait_key', 'text' : style+session_end_txt1})

    else:

        select_session_freq(protocole_session, all_session_random[i])
    





################################
######## TEST TRIG ########
################################


def test_trigger_parralel(parallel_adress):
    port = parallel.ParallelPort(address=parallel_adress)
    for trigger in [1, 2, 4, 255]:
        print('trigger', trigger)
        port.setData(trigger)
        time.sleep(0.5)
        port.setData(0x00)
        time.sleep(1.0)
        
    

################################
######## START PROTOCOL ########
################################


def start_protocolwindow(sujet, num_session, protocol, with_parallel=False, parallel_adress=None):

    log_name = sujet + '_' + str(num_session) + '_LogTrigger_{}.txt'.format(datetime.datetime.now())
    log_name = log_name.replace(':', '-')

    if num_session == 1:
    
        #### write random order
        random_file = sujet + '_' + str(num_session) + '_odor_random_order_{}.txt'.format(datetime.datetime.now())
        random_file = random_file.replace(':', '-')

        random_file_txt = open(random_file,"w")
        random_file_txt.write('Odor randomization for absolute evaluation : \n')
        for i in range(len(odor_num_random)):
                random_file_txt.write(str(odor_num_random[i]) + ' ')
        random_file_txt.close()

    else:
        
        #### write random order
        random_file = sujet + '_' + str(num_session) + '_block_random_order_{}.txt'.format(datetime.datetime.now())
        random_file = random_file.replace(':', '-')

        random_file_txt = open(random_file,"w")
        random_file_txt.write(f'Block randomization for session {str(num_session)} : \n')
        for i in range(len(all_session_random)):
                random_file_txt.write(str(all_session_random[i]) + ' ')
        random_file_txt.close()

    if os.path.exists(log_name):
        os.remove(log_name)

    #### start protocolwindow
    app = mkQApp()
    w = ProtocolWindow(protocol, log_name, with_parallel=with_parallel, parallel_adress=parallel_adress)
    w.show()
    w.start()
    app.exec_()



if __name__ == '__main__':

    #### sujet information
    sujet = 'Pilote'
    num_session = 1
    
    #### protocol selection
#     protocol = debug
#     protocol = protocole_absolute_evaluation
    protocol = protocole_session

    #### trig selection
    #parallel_adress = "0x0378" # LPT1 (en haut bleu)   
    parallel_adress = "0xC030" # LPT2 (en bas noir) 

    #### test trig
#     test_trigger_parralel(parallel_adress)

    #### start
    start_protocolwindow(sujet, num_session, protocol, with_parallel=False, parallel_adress=parallel_adress)

    
