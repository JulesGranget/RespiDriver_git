# -*- coding: utf-8 -*-

from path_stimuli import *


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

#### FR_CV


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
        <p style="font-size:50pt">Fin première partie</p>
</div>
"""

ea_txt6 = """
<div class="center container ">
        <p style="font-size:50pt">Fin première partie</p>
</div>
"""


#### session présentation

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

#### session repiration

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


session_txt2 = f"""
<div class="center container ">
        <p style="font-size:50pt">Respirez par le nez :</p>
        <p><img src="{path_images}/RespiExp_Nez.png" height=320 ></p>
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


######## IMAGE EVALUATION ########

#### début

debut_ie_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début Partie 2 </p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

#### entrainement

entrainement_ie_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de l'évaluation des images</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

entrainement_ie_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur ESPACE</p>
		<p style="font-size:20pt">pour voir l'image</p>
</div>
"""


entrainement_ie_txt3 = f"""
<div class="center container ">
        <p><img src="{path_images}/RespiExp_Nez.png" height=320 ></p>
</div>   
"""

entrainement_ie_txt4 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

entrainement_ie_txt5 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""

entrainement_ie_txt6 = """
<div class="center container ">
        <p style="font-size:50pt">Fin entrainement</p>
</div>
"""


entrainement_ie_txt7 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">pour commencer l'évaluation des images</p>
</div>
"""


entrainement_ie_txt8 = """
<div class="instruction">
        <p style="font-size:20pt">Fin évaluation images</p>
        <p style="font-size:20pt">L'expérimentateur va arriver</p>
</div>
"""



######## EVALUATION SONS ########



#### début

debut_se_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début Partie 3 </p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""



#### entrainement

entrainement_se_txt1 = """
<div class="center container ">
        <p style="font-size:50pt">Début de l'évaluation des sons</p>
</div>

<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p> 
        <p style="font-size:20pt">pour commencer</p>
</div>
"""

entrainement_se_txt2 = """
<div class="center container ">
        <p style="font-size:50pt">Appuyez sur ESPACE</p>
		<p style="font-size:20pt">pour entendre le son</p>
</div>
"""


entrainement_se_txt3 = """
<div class="center container ">
        <p style="font-size:50pt">Période de repos</p>
</div>
"""

entrainement_se_txt4 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">lorsque vous êtes bien reposé·e</p>
</div>
"""

entrainement_se_txt5 = """
<div class="center container ">
        <p style="font-size:50pt">Fin entrainement</p>
</div>
"""


entrainement_se_txt6 = """
<div class="instruction">
        <p style="font-size:20pt">Appuyez sur ESPACE</p>
        <p style="font-size:20pt">pour commencer l'évaluation des sons</p>
</div>
"""


entrainement_se_txt7 = """
<div class="instruction">
        <p style="font-size:20pt">Fin évaluation sons</p>
        <p style="font-size:20pt">L'expérimentateur va arriver</p>
</div>
"""





################################
######## QUESTIONS ########
################################


question_list_STAI = [

    {'label': 'Je me sens calme', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Je me sens tendu(e), crispé(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Je me sens ému(e), bouleversé(e), contrarié(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Je suis décontracté(e), détendu(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Je suis satisfait(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Je suis inquiet, soucieux (inquiète, soucieuse)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},
    {'label': 'Quel niveau d’attention avez-vous porté a votre respiration ?', 'left_label' : 'Très faible', 'right_label': 'Très important'},
    {'label': 'Je suis relaxé(e)', 'left_label' : 'Pas du tout', 'right_label': 'Complètement'},

]


question_list_other_stim = [

	{'label': 'Appréciation', 'left_label' : 'Extrêmement déplaisante', 'right_label': 'Extrêmement plaisant'},
    {'label': 'Eveil', 'left_label' : 'Extrêmement faible', 'right_label': 'Extrêmement intense'},
    {'label': 'Familiarité', 'left_label' : 'Totalement inconnue', 'right_label': 'Extrêmement familière'},
    {'label': 'Intensité', 'left_label' : 'Extrêmement faible', 'right_label': 'Extrêmement fort'},
    {'label': 'Evocation', 'left_label' : "Pas du tout d'accord", 'right_label': "Tout à fait d'accord"},

]

