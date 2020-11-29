#!/usr/bin/env python3
'''
pi
'''
import argparse
import copy
from cv2 import cv2
import imageio
import numpy as np
import simulator


def generate_ppm_file(taille, nb_points, decimale):
    '''
    Cette fonction génère des images
    pour approximer pi de manière
    graphique.
    '''
    image = np.full((taille, taille, 3), 255, dtype="uint8")
    pi_global = 0
    images = []
    for i in range(0, 10):
        pi_estime = simulator.simulator(int(nb_points/10), image)
        images.append(copy.deepcopy(image))
        pi_global += pi_estime
        pi_fin = pi_global/(i+1)
        partie_decimale = int((pi_fin-int(pi_fin))*(10**decimale))
        nb_decimal = f".{decimale}f"
        text = f"{format(pi_fin,nb_decimal)}"
        (text_height, text_width), _ = cv2.getTextSize(text,\
                                       cv2.FONT_HERSHEY_SIMPLEX, 2, 5)
        cv2.putText(images[i],text, (int(taille/2-text_height/2),\
                                     int(taille/2+text_width/2)),\
                                     cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)
        imageio.imwrite(f"out/img{i}_{int(pi_fin)}-{partie_decimale}.png", image)
    imageio.mimsave('out/gif_seb.gif', images, duration=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)
    arguments = parser.parse_args()
    generate_ppm_file(arguments.taille_image, arguments.nombre_de_point, \
                      arguments.nombre_chiffre_virgule)
