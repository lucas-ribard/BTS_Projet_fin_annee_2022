# Projet de fin d'année de BTS SN 

C'est mon premier "vrais projet", il n'est pas beau, et est encore moins optimisé mais il fonctionne(ait en Mai 2022).  
*Il nécessite la librairie Opencv et une caméra pour fonctionner*

## Robot Ramasseur de Fruits

![image](https://user-images.githubusercontent.com/114387855/217528862-367dd758-f2fc-4aed-8b9b-07fa2f0d1f74.png)

### Partie Déplacement autonome

Le but de ce projet est de contrôler un robot agricole autonome, ce code s'exécutait dans une raspberry pi 3 b+ à bord du robot.
Le robot observait le champ via une caméra monté sur le châssis et à l'aide des filtres, détecte chaque plant individuellement et utilise leurs positions pour déterminer la direction dans lequel aller.  

Le robot se sert des contours des plants pour déduire leurs centres :  

![1](https://user-images.githubusercontent.com/114387855/217525477-ea6a3c24-a3e7-46d2-9448-10f401cffa30.PNG)

Il se sert ensuite de l'algorithme de régression linéaire pour en déduire la direction du champ, et se sert de sa base pour former un angle.  
  
On utilise ensuite cet angle pour déterminer les corrections de direction à faire pour être dans le sens du champ :

![image](https://user-images.githubusercontent.com/114387855/217526705-bdcb7a93-0a77-44b6-9b61-8ad0f8e40514.png)
![image](https://user-images.githubusercontent.com/114387855/217526459-30b37322-5c09-43d3-b25d-82cd75468ae1.png)

Les instructions sont ensuite transférés à l'arduino qui contrôle les moteurs.

![image](https://user-images.githubusercontent.com/114387855/217527997-d8270287-a21f-4225-b11e-a48dfcfbd3dd.png)
