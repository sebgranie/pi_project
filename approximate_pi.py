#!/usr/bin/env python3
'''
Ce programme permet de générer des images ppm marquées par une approximation
courante de la valeur de π puis les convertir pour afficher un gif.
'''
import argparse
import copy
import os
import subprocess
from cv2 import cv2
import imageio
import numpy as np
import simulator

class PiEstimator:
    '''
    Cette classe permet d'encapsuler l'estimation de pi et
    ainsi mieux structurer les fonctions utilisées, alléger
    les notations et réduire le nombre de variables utilisées.
    '''
    def __init__(self):
        self.iteration = 0.0
        self.sum_pi = 0.0

    def add_new_pi_estimate(self, pi_estimation):
        '''
        Cette méthode permet d'effectuer un
        calcul de moyenne de pi afin de converger
        vers la valeur la plus juste possible.
        '''
        self.sum_pi += pi_estimation
        self.iteration += 1
        return self.sum_pi / self.iteration

def validate_all_arguments(arguments):
    '''
    Cette fonction vérifie la validité des arguments en entrée du programme.
    '''
    image_max_size = 3840
    if arguments.taille_image < 0 or arguments.taille_image > image_max_size:
        raise ValueError(f"La taille de l'image doit etre comprise entre [0, {image_max_size}].")
    max_nombre_de_points = 1e7
    if arguments.nombre_de_point < 0 or arguments.nombre_de_point > max_nombre_de_points:
        raise ValueError(f"Le nombre de points total de l'image doit etre compris entre\
                        [0, {max_nombre_de_points}].")
    max_nombre_chiffre_virgule = 7
    if arguments.nombre_chiffre_virgule < 0 or \
        arguments.nombre_chiffre_virgule > max_nombre_chiffre_virgule:
        raise ValueError(f"Le nombre de chiffres apres la virgule doit \
                        etre compris entre [0, {max_nombre_chiffre_virgule}].")


def generate_all_ppm_files(taille, nb_points, decimale):
    '''
    Cette fonction génère des images de manière itérative. Elles représentent
    la répartition des points obtenus aléatoirement par la fonction simulation().
    Cette fonction utilise les calculs réalisés dans la fonction generate_ppm_file()
    pour afficher une approximation de la valeur de pi sur l'image.
    '''
    create_or_clean_folder("./out")
    # Creation d'une image carré blanche
    image = np.full((taille, taille, 3), 255, dtype="uint8")
    pi_estimator = PiEstimator()
    for i in range(0, 10):
        generate_ppm_file(image, pi_estimator, int(nb_points/10), i, decimale)

def generate_ppm_file(image, pi_estimator, nb_points_par_image, i, decimale):
    '''
    Cette fonction permet de générer une image au format ppm. Elle appelle
    la fonction simulation lui permettant de générer des points aléatoirement.
    Chaque estimation receuillie permet grâce à la méthode add_new_pi_estimate
    d'obtenir des valeurs convergentes vers pi. La valeur est ensuite écrite
    sur l'image créée et sauvegardée dans le dossier appelée out.
    '''
    # 1 - Obtention de l'estimation de pi
    list_blue, list_pink = [], []
    pi_estime = simulator.simulator(nb_points_par_image, list_blue, list_pink)

    # 2 - Coloration des pixels de l'image en fonction de leur distance au centre.
    color_image_with_points(image, list_blue, list_pink)

    # 3 - Nouvelle estimation ajoutée pour actualiser la moyenne globale
    pi_val = pi_estimator.add_new_pi_estimate(pi_estime)
    print(f'{pi_estime} - {pi_val}')
    # 4 - Affichage de l'estimation de pi sur l'image
    # La copie entière de l'image permet d'écrire le nombre pi
    # sur celle-ci avant de la sauvegarder au format ppm.
    copie_image = copy.deepcopy(image)
    nb_decimal = f".{decimale}f"
    write_pi_on_image(copie_image, pi_val, nb_decimal)

    # 5 - Sauvegarde de l'image sur le disque dur
    partie_decimale = int((pi_val-int(pi_val))*(10**decimale))
    imageio.imwrite(f"out/img{i}_{int(pi_val)}-{partie_decimale}.ppm", copie_image)

def color_image_with_points(image, points_bleu, points_rose):
    '''
    Cette fonction affecte la couleur bleu sur chaque pixel appartenant au
    cercle de rayon 1 et la couleur rose à tous les autres pixels de l'image.
    '''
    demi_taille = image.shape[0]//2
    for coordonnes in points_bleu:
        image[int((coordonnes[0]+1)*demi_taille)]\
             [int((coordonnes[1]+1)*demi_taille)] = (0, 0, 255)
    for coordonnes in points_rose:
        image[int((coordonnes[0]+1)*demi_taille)]\
             [int((coordonnes[1]+1)*demi_taille)] = (238, 130, 238)

def write_pi_on_image(image, pi_val, nb_decimal):
    '''
    Cette fonction permet d'écrire la valeur
    de pi sur l'image spécifiée en paramètre.
    '''
    taille = image.shape[0]
    text = f"{format(pi_val ,nb_decimal)}"

    (text_height, text_width), _ = cv2.getTextSize(text,\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, 5)
    cv2.putText(image, text, (int(taille/2-text_height/2),\
                                    int(taille/2+text_width/2)),\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)

def generate_gif(ppm_folder):
    '''
    Cette fonction utilise le module subprocess pour créer un gif
    à partir de toutes les images ppm dans un dossier donné.
    '''
    subprocess.call(f"convert -delay 100 -loop 0 ./{ppm_folder}/img*.ppm ./{ppm_folder}/pi.gif",\
                    shell=True)

def create_or_clean_folder(path):
    '''
    Cette fonction crée un dossier s'il n'existe pas déjà sans
    lancer d'erreurs et supprime son contenu s'il existe deja.
    '''
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
        return

    filelist = [f for f in os.listdir(path) if (f.endswith(".ppm") or f.endswith(".gif"))]
    for filename in filelist:
        os.remove(os.path.join(path, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)
    arguments = parser.parse_args()
    validate_all_arguments(arguments)
    generate_all_ppm_files(arguments.taille_image, arguments.nombre_de_point,\
                            arguments.nombre_chiffre_virgule)
    generate_gif("out")
