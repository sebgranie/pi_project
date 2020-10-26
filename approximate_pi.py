#!/usr/bin/env python3

import argparse
import simulator
import imageio
import numpy as np


def generate_ppm_file(taille, nb_points, decimale):
    image = np.zeros((taille, taille, 3), dtype="uint8")
    simulator.simulator(nb_points, image)
    imageio.imwrite("image_pi.jpg", image)
    







if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)


    arguments = parser.parse_args()

    generation_image = generate_ppm_file(arguments.taille_image, arguments.nombre_de_point, arguments.nombre_chiffre_virgule)
    # simulator = simulator(arguments.nombre_de_point, image)