# pi_project

## 1. Code

[Lien Github vers notre code hébergé en ligne](https://github.com/sebgranie/projet_pi)

### 1.1. Dependences

- **Python3**

J'ai utilisé Python3 pour réaliser ce projet. Veuillez vérifier que vous ayez cette version installée avant d'executer le code. Pour verifier que Python3 est bien installé sur votre systèm, exécutez:

```
python3 --version
```

Vous devriez avoir un résultat qui commence par 3. Exemple:

```
Python3 3.8.5
```

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

### 1.2. Diagramme de classe

Voici le diagramme de classe representant l'architecture du code.

diagramme à insérer

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

Ce projet se divise en l'implémentation d'un module `simulator.py` et d'un programme `approximate_pi.py`. \
Mon idée a été de générer, à partir du module python `random` et de sa méthode `uniform`, un nombre flottant entre -1 et 1, c'est à dire dans un carré de coté de longueur 2. Une fois ces points générés, je calcule la distance entre le centre de l'image de coordonnées (0,0) et chacun de ces points par la formule classique: \
![Formule de la distance entre deux points](distance_image.png)

Si l'image est spécifiée dans l'appel du module `simulator.py`, l'ensemble des points dont la distance au centre de l'image est inférieure à 1, le pixel attribué à ce point est colorié par un code RGB d'une variante de bleu. Pour les autres, une variante de rose y est appliquée. Pour faire cette coloration, j'utilise la variable `image` qui est une matrice de dimension la taille de l'image dont chacun de ses composantes est un tuple de 3 valeurs lié au code RGB.\
Par ailleurs, un compteur est incrémenté pour tous points appartenant au cercle de rayon 1 et de centre (0,0).\
On renvoie donc 4 fois la probabilité qu'un point se situe dans chacun des 4 quarts de cercle, or cette probabilité vaut le rapport entre la valeur du compteur divisé par l'ensemble des points tirés.
