#!/usr/bin/env python3
'''
pi
'''
import argparse
import copy
from cv2 import cv2
import imageio
import numpy as np
import os
import simulator
import subprocess

class PiEstimator(object):
    def __init__(self):
        self.iteration = 0
        self.sum_pi = 0

    def AddNewPiEstimate(self, pi_estimation):
        self.sum_pi += pi_estimation
        self.iteration += 1
        print(self.iteration)
        return self.sum_pi / self.iteration


def generate_all_ppm_files(taille, nb_points, decimale):
    '''
    Cette fonction génère des images
    pour approximer pi de manière
    graphique.
    '''
    # Creation d'une image carré blanche
    image = np.full((taille, taille, 3), 255, dtype="uint8")
    pi_estimator = PiEstimator()

    # images = []
    create_folder("./out")
    for i in range(0, 10):
        generate_ppm_file(image, pi_estimator, int(nb_points/10), i, decimale)

def generate_ppm_file(image, pi_estimator, nb_points_par_image, i, decimale):
    taille = image.shape[0]
    pi_estime = simulator.simulator(nb_points_par_image, image)
    copie_image = copy.deepcopy(image)
    pi = pi_estimator.AddNewPiEstimate(pi_estime)
    partie_decimale = int((pi-int(pi))*(10**decimale))
    nb_decimal = f".{decimale}f"
    text = f"{format(pi,nb_decimal)}"
    (text_height, text_width), _ = cv2.getTextSize(text,\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, 5)
    cv2.putText(copie_image, text, (int(taille/2-text_height/2),\
                                    int(taille/2+text_width/2)),\
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)
    imageio.imwrite(f"out/img{i}_{int(pi)}-{partie_decimale}.ppm", copie_image)

def generate_gif(ppm_folder):
    subprocess.call(f"convert -delay 100 -loop 0 ./{ppm_folder}/img*.ppm ./{ppm_folder}/pi.gif", shell=True)
    # imageio.mimsave('out/gif_seb.gif', images, duration=1)

def create_folder(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)
    arguments = parser.parse_args()
    generate_all_ppm_files(arguments.taille_image, arguments.nombre_de_point, \
                      arguments.nombre_chiffre_virgule)
    generate_gif("out")

