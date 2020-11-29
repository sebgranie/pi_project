# pi_project

## 1. Code

[Lien Github vers notre code hébergé en ligne](https://github.com/sebgranie/projet_pi)

### 1.1. Dependences

- **Python3**

Nous avons utilisé Python3 pour réaliser ce projet. Veuillez vérifier que vous ayez cette version installée avant d'executer le code. Pour verifier que Python3 est bien installé sur votre systèm, exécutez:

```
python3 --version
```

Vous devriez avoir un résultat qui commence par 3. Exemple:

```
Python3 3.8.5
```

- **numpy**

Nous avons choisi d'utiliser la librairie `numpy` afin de faciliter la manipulation de matrices dans la fonction de calcul de la distance entre deux mots `CalculDistanceMots()`.

Installation:

```
pip3 install numpy
```

### 1.2. Diagramme de classe

Voici le diagramme de classe representant l'architecture du code.

diagramme à insérer

### 1.3. Execution

Executer les commandes suivantes dans le terminal au niveau du dossier `projet_info_correcteur` où se trouvent tous les fichiers requis par le programme:
Nous accèderons aux fichiers sources et ressources grâce à des chemins relatifs comme montré ci-dessous.
Nous utiliserons le texte `exemple1.txt` comme exemple de texte à corriger.

#### 1.4.1 approximate_pi :

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

pack insatll:
sudo apt install graphicsmagick-imagemagick-compat
pip3 install opencv-python
pip3 install imageio
