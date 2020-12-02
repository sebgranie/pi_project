#!/usr/bin/env python3
'''
Ce programme permet de générer des images ppm marquée par une approximation
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
        self.iteration = 0
        self.sum_pi = 0

    def add_new_pi_estimate(self, pi_estimation):
        '''
        Cette méthode permet d'effectuer un
        calcul de moyenne de pi afin de converger
        vers la valeur la plus juste possible.
        '''
        self.sum_pi += pi_estimation
        self.iteration += 1
        print(self.iteration)
        return self.sum_pi / self.iteration


def generate_all_ppm_files(taille, nb_points, decimale):
    '''
    Cette fonction génère des images de manière itérative.
    Elles représentent la répartition des points obtenus
    aléatoirement par la fonction simulation().
    Cette fonction utilise les calculs réalisés dans la
    fonction generate_ppm_file() pour afficher une
    approximation de la valeur de pi sur l'image.
    '''
    # Creation d'une image carré blanche
    image = np.full((taille, taille, 3), 255, dtype="uint8")
    pi_estimator = PiEstimator()
    create_folder("./out")
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
    taille = image.shape[0]
    pi_estime = simulator.simulator(nb_points_par_image, image)
    copie_image = copy.deepcopy(image)
    pi_val = pi_estimator.add_new_pi_estimate(pi_estime)
    partie_decimale = int((pi_val-int(pi_val))*(10**decimale))
    nb_decimal = f".{decimale}f"
    text = f"{format(pi_val ,nb_decimal)}"
    (text_height, text_width), _ = cv2.getTextSize(text,\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, 5)
    cv2.putText(copie_image, text, (int(taille/2-text_height/2),\
                                    int(taille/2+text_width/2)),\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)
    imageio.imwrite(f"out/img{i}_{int(pi_val)}-{partie_decimale}.ppm", copie_image)

def generate_gif(ppm_folder):
    '''
    Cette fonction utilise le module subprocess pour créer un gif à partir de
    toutes les images ppm dans un dossier donné.
    '''
    subprocess.call(f"convert -delay 100 -loop 0 ./{ppm_folder}/img*.ppm ./{ppm_folder}/pi.gif",\
                    shell=True)

def create_folder(path):
    '''
    Cette fonction crée un dossier s'il n'existe
    pas déjà sans relever d'erreurs.
    '''
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)
    arguments = parser.parse_args()
    generate_all_ppm_files(arguments.taille_image, arguments.nombre_de_point,\
                            arguments.nombre_chiffre_virgule)
    generate_gif("out")
