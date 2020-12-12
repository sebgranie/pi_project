# Projet Pi

## 1. Code

[Lien Github vers notre code hébergé en ligne](https://github.com/sebgranie/pi_project)

### 1.1. Dependences

- **numpy**

J'ai choisi d'utiliser la librairie `numpy` afin de faciliter la manipulation de matrices dans la fonction `generate_all_ppm_files()` spécifiquement lors de la création d'une image initialement blanche.

Installation:

```
pip3 install numpy
```

- **imageio**

Installation:

```
pip3 install imageio
```

- **opencv**

Installation:

```
pip3 install opencv-python
```

- **pylint**

Installation:

```
sudo apt install pylint
```

- **convert**

Installation:

```
sudo apt install graphicsmagick-imagemagick-compact
```

### 1.3. Execution

Executer les commandes suivantes dans le terminal au niveau du dossier `projet_pi` où se trouvent tous les fichiers requis par le programme:

#### 1.3.1 Approximate_pi :

La commande suivante permet de lister les arguments obligatoires et optionnels de ce programme:

```sh
python3 approximate_pi.py --help
```

Pour executer le programme:

```sh
python3 approximate_pi.py taille_image \
                          nombre_de_points \
                          nombre_chiffre_virgule \
```

#### Structure et explication

- Procédurales
- Encapsulation de l'estimation de pi grâce à la classe `PiEstimateur`
-

Ce projet se divise en l'implémentation d'un module `simulator.py` et d'un programme `approximate_pi.py`.

### Module simulator.py :

L'objectif de ce module est de renvoyer une estimation de la valeur de pi, pour cela j'ai appliqué la méthode de Monte-Carlo à partir du module python `random` et de sa méthode `uniform`dans l'intervalle [-1, 1]. Une fois ces points générés, je calcule la distance entre le centre de l'image de coordonnées (0,0) et chacun de ces points par la formule classique: \
![Formule de la distance entre deux points](distance_image.png)

Un compteur est incrémenté pour tous les points appartenant au cercle de rayon 1 et de centre (0,0).\
Par la méthode de Monte-Carlo nous pouvons prouver qu'en réalisant cette expérience de tirage sur une surface égale à un quart de cercle, cela permet d'estimer la valeur de `pi/4`. Finalement, ce module renvoie donc 4 fois la probabilité qu'un point se situe dans chacun des 4 quarts de cercle. Cette probabilité vaut le rapport entre la valeur du compteur divisé par l'ensemble des points tirés.

Une fois la première partie du sujet complétée, j'ai voulu réutiliser le module `simulator.py` afin de réaliser la seconde partie du sujet.
L'appel de la fonction simulator a reçu un nouveau paramètre optionnel qui est une image. Si celle-ci est spécifiée, chacun des points tirés aléatoirement sera associé à un pixel de l'image grâce à une règle de trois afin d'établir une relation entre l'intervalle [-1, 1] et les dimensions de l'image. Ce paramètre étant renseigné lors de l'appel du programme principal.

Cette image est crée avec le module `numpy` sous forme d'une matrice de taille : `taille_image`. Chaque valeur de la matrice représente un pixel de l'image, j'ai donc décidé que chacune de ces valeurs prennent la forme d'un tuple de trois valeurs, conforme au format de couleur RGB. La couleur de chaque pixel sera fonction de sa distance au centre de l'image. Tous points dont la distance est inférieure à 1 sera `(0, 0, 255) = bleu`, les autres `(238, 130, 238) = rose`.

### Programme principal approximate_pi.py :

Ce programme se décompose en plusieurs fonctions:

- `generate_ppm_file()`
- `generate_all_ppm_files()`
- `generate_gif()`
- `create_or_clean_folder()`

L'objectif est de produire une visualisation de l'état de convergence de l'algorithme de Monte-Carlo pour l'estimation du nombre pi.
Celui-ci va réutiliser le module `simulator.py`
Création d'estimation de pi indépendantes entre elles, afin de permettre la convergence des estimations, j'ai réalisé une moyenne itérative mise à jour après chaque appel du module `simulator.py` qui permet de converger vers la juste valeur de pi.
Pour cela, j'utilise une classe `PiEstimator` permettant d'encapsuler le calcul de pi pour que chaque fonction est un but défini. Cela permet notamment à `generate_ppm_file` de se focaliser sur l'affichage de l'estimation calculée dans le moduleet en alléger les notations.\ La fonction `generate_ppm_file()`stocke tout d'abord la taille de l'image qui sera utilisé dans le module`simulator.py`comme expliqué précedemment.\ Une estimation de la valeur de pi est exécuté en appelant le module`simulator.py`puis est ajoutée à la variable`sum_pi`afin d'obtenir des valeurs convergentes au fur et à mesure des estimations réalisées grâce à la méthode`add_new_pi_estimate()`. L'image est ensuite copié afin d'éviter de réecrire le nombre pi sur la même image.\ J'ai ensuite réussi à stockée la partie entière des estimations d'une part et la partie décimale d'autre part dans le but de les intégrer à la fois sur l'image elle-même comme demandé mais également pour que le nom de l'image soit au format `img0_3-13776`.
