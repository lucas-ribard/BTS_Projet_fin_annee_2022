# Projet de fin d'année de BTS SN 

C'est mon premier "vrais projet", il n'est pas parfait ni optimisé mais il fonctionne(ait en Mai 2022).  
*Il nécessite la librairie Opencv et une caméra pour fonctionner*

## Robot Ramasseur de Fruits
Le but de ce projet est de prototiper un robot agricole autonome, capable de se déplacer seul dans des champs et de ramasser les fruit considéré comme murs. 
  
![image](https://user-images.githubusercontent.com/114387855/217528862-367dd758-f2fc-4aed-8b9b-07fa2f0d1f74.png)
### Ce projet est divisé en 5 parites différentes :  
#### Chassis et moteurs / Télécommande / Bras / Déplacement autonome / Collection de données  
  
Je ne vais présenter que la partie que j'ai réalisé :  
### Partie Déplacement autonome  
  
Ce code s'exécutait dans une raspberry pi 3 b+ à bord du robot.
Le robot observait le champ via une caméra monté sur le châssis et à l'aide des filtres, détecte chaque plant individuellement et utilise leurs positions pour déterminer la direction dans lequel aller.  

Le robot utilise des filtres de couleur pour isoler chaque plant, et se sert des contours des plants pour déduire leurs centres :  

![1](https://user-images.githubusercontent.com/114387855/217525477-ea6a3c24-a3e7-46d2-9448-10f401cffa30.PNG)

Les Coordonnées des plants sont stockées dans deux array, ArrayX et ArrayY, et sont ensuite utilisé avec un algorithme de régression linéaire pour en déduire la direction du champ, et se sert de sa base pour former un angle.  

![217525477-ea6a3c24-a3e7-46d2-9448-10f401cffa30](https://github.com/lucas-ribard/BTS_Projet_fin_annee_2022/assets/114387855/1c0f072c-38f1-47f7-aa8a-26cfd2730205)

On utilise ensuite cet angle pour déterminer les corrections de direction à faire pour rester dans le sens du champ :

![image](https://user-images.githubusercontent.com/114387855/217526705-bdcb7a93-0a77-44b6-9b61-8ad0f8e40514.png)
![image](https://user-images.githubusercontent.com/114387855/217526459-30b37322-5c09-43d3-b25d-82cd75468ae1.png)
  
La façon dont le robot est assemblé le force a se déplacer comme un char, les instructions sont donc formés de la maniere suivante :  
● une Variable booléenne pour l'activation des moteurs droit.  
● une Variable booléenne pour le sens de rotation des moteurs droit.  
● une Variable booléenne pour l'activation des moteurs gauche.  
● une Variable booléenne pour le sens de rotation des moteurs gauche.  
  
Les instructions sont ensuite transférés à l'arduino qui contrôle les moteurs.

![image](https://user-images.githubusercontent.com/114387855/217527997-d8270287-a21f-4225-b11e-a48dfcfbd3dd.png)
