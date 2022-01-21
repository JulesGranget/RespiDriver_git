# -*- coding: utf-8 -*-

############ ici on annote la frequence moyenne du sujet enregistree sur le fichier trc au calme - chiffre issu du script plot-resp-distribution
freq_confort = .218


# from patient_params import *

# durée du bloc présentation
duree_presentation = 20
# durée du bloc entrainement
duree_entrainement = 40
# durée des blocs confort , 0.15, 0.5 , AMPLE, Bouche
duree_blocs = 300
# durée des périodes de repos
duree_repos = 20


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

# Exemple de Sam

# txt1 = """
# <div class="center container ">
#         <p style="font-size:70pt">Yep</p>
#         <p><img src="img/test.png"></p>
# </div>
# """



# txt1 = questionnaire

txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Nez</p>
        <p><img src="RespiExp_Nez.png" height=320 ></p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">pour continuer</p>
</div>

"""

# txt3 = presentation_respidriver

txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Avez vous des questions ?</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur espace lorsque vous</p>
        <p style="font-size:20pt">souhaitez démarrer la session d’entrainement</p>
</div>

"""

# Session d'entrainement

txt5 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur ESPACE pour</p>
        <p style="font-size:50pt">démarrer une nouvelle session</p>
</div>
"""

txt6_nez = """
<div class="center container ">
        <p style="font-size:50pt">Respirez par le nez :</p>
        <p><img src="RespiExp_Nez.png" height=320 ></p>
</div>   

<div class="instruction">      
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour lancer le logiciel de respiration</p> 
</div>
"""

txt6_bouche = """
<div class="center container ">
        <p style="font-size:50pt">Respirez par la bouche :</p>
        <p><img src="RespiExp_Bouche.png" height=240></p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour lancer l'enregistrement</p>  
</div>
"""

txt6_bouche_free = """
<div class="center container ">
        <p style="font-size:50pt">Respirez par la bouche :</p>
        <p><img src="RespiExp_Bouche.png" height=240></p>
</div>
"""

# txt7 = Respi_driver_test

txt8 = """
<div class="center container ">
        <p style="font-size:50pt">Session terminée</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour accéder au questionnaire</p>
</div>
"""

# txt9 = Questionnaire_complet

txt10 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

txt11 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""

txt12 = """
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

# Fin session d'entrainement

txt13 = """
<div class="center container ">
        <p style="font-size:50pt">Premiere partie terminee</p>
        <p style="font-size:50pt">Merci de votre participation</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Veuillez faire signe aux experimentateurs</p>
        <p style="font-size:20pt">pour passer a la suite</p>

</div>
"""

# Fin première partie

txt14 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur espace pour démarrer la</p>
        <p style="font-size:50pt">Session AMPLE</p>

</div>
"""

# Fin session ample

txt15 = """
<div class="center container ">
        <p style="font-size:50pt">Session terminee</p>
        <p style="font-size:50pt">Merci de votre participation</p>

<div class="instruction">
        <p style="font-size:20pt">Veuillez faire signe aux experimentateurs</p>
        <p style="font-size:20pt">pour passer a la suite</p>

</div>
"""
# Transition

txt16 = """

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur espace pour</p>
        <p style="font-size:20pt">lancer l'entrainement AMPLE</p>

</div>
"""


txt20 = """
<div class="center container ">
        <p style="font-size:50pt">Présentation du</p>
        <p style="font-size:50pt">logiciel de respiration</p>
        <p style="font-size:50pt">Merci pour votre participation</p>
        <p style="font-size:50pt">Vous pouvez stopper l'expérience</p>
        <p style="font-size:50pt">lorsque vous le souhaitez</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer la présentation</p>
</div>
"""

txt21 = """
<div class="center container ">
        <p style="font-size:50pt">Présentation terminée</p>
        <p style="font-size:50pt">Avez vous des questions ?</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE lorsque vous</p>
        <p style="font-size:20pt">souhaitez démarrer la prochaine session</p>
</div>

"""

txt22 = """

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE lorsque vous</p>
        <p style="font-size:20pt">souhaitez démarrer la session</p>
</div>

"""


txt23 = """

<div class="center container ">
        <p style="font-size:50pt">Session Terminée</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE lorsque vous</p>
        <p style="font-size:20pt">souhaitez démarrer la session suivante</p>
</div>

"""

txt24 = """

<div class="center container ">
        <p style="font-size:50pt">Session Terminée</p>
        <p style="font-size:50pt">Faites signe aux expérimentateurs</p>
</div>


"""

txt25 = """

<div class="center container ">
        <p style="font-size:50pt">Appuyez sur ESPACE</p>
        <p style="font-size:50pt">pour accéder au questionnaire AMPLE</p>
</div>


"""

#Fin deuxième partie

txt26 = """
<div class="center container ">
        <p style="font-size:50pt">Deuxième partie terminée</p>
        <p style="font-size:50pt">Merci de votre participation</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Veuillez faire signe aux expérimentateurs</p>
        <p style="font-size:20pt">pour passer à la suite</p>

</div>
"""

#Démarrer bouche
txt27 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur espace pour démarrer la</p>
        <p style="font-size:50pt">Session BOUCHE</p>

</div>
"""


# Exemple de Sam :

# steps = [
#     {'type': 'display', 'duration': 4, 'text' : style+txt1},
#     {'type': 'display', 'duration': 'wait_key', 'text' : style+txt2},
#     {'type': 'respidriver', 'duration':5, 'params' : {'freq1' : .15, 'freq2':.2, 'cycle_duration':60, 'resp_ratio' : .4, 'left_pad': 3.}},
#     {'type': 'display', 'duration': 2., 'text' : txt3},
# ]




question_list1 = [
    {'label': 'Avez-vous faim ?', 'left_label' : 'Très peu', 'right_label': 'Extrêmement'},
    {'label': 'Quel est votre niveau de relaxation ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de stress ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de fatigue ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel niveau d’attention avez-vous porté a votre respiration ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
]

question_list2 = [
    {'label': 'Avez-vous eu des difficultés à suivre le logiciel de respiration ?', 'left_label' : 'Très peu', 'right_label': 'Extrêmement'},
    {'label': 'Quel est votre niveau de relaxation ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de stress ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de fatigue ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel niveau d’attention avez-vous porté au logiciel de respiration ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
]

question_list3 = [

    {'label': 'Quel est votre niveau de relaxation ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de stress ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel est votre niveau de fatigue ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Quel niveau d’attention avez-vous porté a votre respiration ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},

]



block_présentation = [
        {'type': 'question', 'question_list': question_list1},   
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt2},
        {'type': 'respidriver', 'duration':40, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},    
        {'type': 'respidriver', 'duration':30, 'params' : {'freq1' : .10, 'freq2':.10, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt4},
]

block_entrainement = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':100},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':30, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':101},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':102},
    {'type': 'question', 'question_list': question_list2},
    {'type': 'display', 'duration': 20, 'text' : style+txt10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt12},

]

    # Début expérience

block_15 = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : .15, 'freq2':.15, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':12},
    {'type': 'question', 'question_list': question_list2, 'trigger' :13},
    {'type': 'display', 'duration': 20, 'text' : style+txt10, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :15},

]

block_confort = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':30},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : .3, 'freq2':.3, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':31},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':32},
    {'type': 'question', 'question_list': question_list2, 'trigger' :33},
    {'type': 'display', 'duration': 20, 'text' : style+txt10, 'trigger' :34},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :35},

]

block_50 = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':50},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':51},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':52},
    {'type': 'question', 'question_list': question_list2, 'trigger' :53},
    {'type': 'display', 'duration': 20, 'text' : style+txt10, 'trigger' :54},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :55},

]

fin_premiere_partie = [

        {'type': 'display', 'duration': 5, 'text' : style+txt13, 'trigger' :4},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt13, 'trigger' :5},

]

block_entrainementAMPLE = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':200},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':201},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':202},
    {'type': 'question', 'question_list': question_list2},
    {'type': 'display', 'duration': 20, 'text' : style+txt10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt12},

]

block_AMPLE = [

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':60},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':61},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':62},
    {'type': 'question', 'question_list': question_list2, 'trigger' :63},
    {'type': 'display', 'duration': 20, 'text' : style+txt10, 'trigger' :64},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :65},
    
    
    
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':60},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':180, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':61},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':62},
    {'type': 'question', 'question_list': question_list2},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15},

]

questionnaire_ample = [

        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt25},
        {'type': 'question', 'question_list': question_list3},
]

block_Bouche = [

        {'type': 'display', 'duration': 10, 'text' : style+txt6_bouche_free, 'trigger':70},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_bouche, 'trigger':71},
        {'type': 'display', 'duration': duree_blocs, 'text' : style+txt6_bouche_free, 'trigger':72},
        {'type': 'question', 'question_list': question_list3},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15}
                
]

        # Protocoles

debug = [

        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':100},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
        {'type': 'respidriver', 'duration':20, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':1},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':2},
        {'type': 'question', 'question_list': question_list2},
        {'type': 'display', 'duration': 20, 'text' : style+txt10},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt12},
        
]

protocole_patient = [

# block_présentation

        {'type': 'question', 'question_list': question_list1},   
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt2},
        {'type': 'respidriver', 'duration':duree_presentation, 'params' : {'freq1' : .25, 'freq2':.25, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},    
        #~ {'type': 'respidriver', 'duration':30, 'params' : {'freq1' : .10, 'freq2':.10, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt4},

# block_entrainement
        
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':100},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
        {'type': 'respidriver', 'duration':duree_entrainement, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':101},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':102},
        {'type': 'question', 'question_list': question_list2},
        {'type': 'display', 'duration': duree_repos, 'text' : style+txt10},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt12},


# block_confort 

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':30},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':31},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':32},
    {'type': 'question', 'question_list': question_list2, 'trigger' :33},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :34},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :35},

# block_15

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : .15, 'freq2':.15, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':12},
    {'type': 'question', 'question_list': question_list2, 'trigger' :13},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :15},

# block_confort 

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':30},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':31},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':32},
    {'type': 'question', 'question_list': question_list2, 'trigger' :33},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :34},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :35},

# block_15

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : .15, 'freq2':.15, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':12},
    {'type': 'question', 'question_list': question_list2, 'trigger' :13},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :15},

# block_50 

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':50},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':51},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':52},
    {'type': 'question', 'question_list': question_list2, 'trigger' :53},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :54},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :55},

# block_15

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':10},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : .15, 'freq2':.15, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':11},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':12},
    {'type': 'question', 'question_list': question_list2, 'trigger' :13},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :14},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :15},

# block_50 

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt5, 'trigger':50},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : .5, 'freq2':.5, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':51},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':52},
    {'type': 'question', 'question_list': question_list2, 'trigger' :53},
    {'type': 'display', 'duration': duree_repos, 'text' : style+txt10, 'trigger' :54},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt11, 'trigger' :55},


# fin_premiere_partie 

        {'type': 'display', 'duration': 5, 'text' : style+txt13, 'trigger' :4},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt13, 'trigger' :5},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt16, 'trigger':2},

# block_entrainementAMPLE

    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':200},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_entrainement, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8},
    {'type': 'question', 'question_list': question_list2},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt12},

# block_AMPLES 
  
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':60},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':61},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':62},
    {'type': 'question', 'question_list': question_list2, 'trigger' :64},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15},

# block_Bouche

        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt27, 'trigger':70},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_bouche},
        {'type': 'display', 'duration': duree_blocs, 'text' : style+txt6_bouche_free, 'trigger':71},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':72},
        {'type': 'question', 'question_list': question_list3, 'trigger':74},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15}

]

debug = [

  
# block_AMPLES 
  
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt14, 'trigger':60},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_nez},
    {'type': 'respidriver', 'duration':duree_blocs, 'params' : {'freq1' : freq_confort, 'freq2': freq_confort, 'cycle_duration':30, 'resp_ratio' : .4, 'left_pad': 6.}, 'trigger':61},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':62},
    {'type': 'question', 'question_list': question_list2, 'trigger' :64},
    {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15},

# block_Bouche

        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt27, 'trigger':70},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt6_bouche},
        {'type': 'display', 'duration': duree_blocs, 'text' : style+txt6_bouche_free, 'trigger':71},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt8, 'trigger':72},
        {'type': 'question', 'question_list': question_list3, 'trigger':74},
        {'type': 'display', 'duration': 'wait_key', 'text' : style+txt15}

]

def start_protocolwindow():
    from myqt import QT, mkQApp
    import datetime
    import os
    from protocolwindow import ProtocolWindow
    
    log_name = 'LogTrigger {}.txt'.format(datetime.datetime.now())
    log_name = log_name.replace(':', '-')

    if os.path.exists(log_name):
        os.remove(log_name)

#     protocol = debug
    protocol = protocole_patient


    # serial_port = 'COM3'
#     serial_port = 'COM6'    
#     with_serial = True
    
    serial_port = None
    with_serial = False

    app = mkQApp()
    w = ProtocolWindow(protocol, log_name, with_serial=with_serial, serial_port=serial_port)
    w.show()
    w.start()
    app.exec_()

#     with_parallel = False
#     #with_parallel = True
    
#     ### LPT1 (en haut bleu): "0x0378"
#     # parallel_adress = "0x0378"
    
#     ### LPT2 (en bas noir) : "0xC030"    
#     parallel_adress = "0xC030"

#     app = mkQApp()
#     w = ProtocolWindow(protocol, log_name, with_parallel=with_parallel, parallel_adress=parallel_adress)
#     w.show()
#     w.start()
#     app.exec_()

if __name__ == '__main__':
    
    start_protocolwindow()
    
