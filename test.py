#!/usr/bin/env python3
'''
Ce module m'a permit de réaliser mes tests sur le
programme approximate_pi.py, afin de recueillir des
données que j'ai exploitées dans le module data_graph.py.
'''
from approximate_pi import *
import time

class Arguments:
    def __init__(self, taille_image, nombre_de_point, nombre_chiffre_virgule):
        self.taille_image = int(taille_image)
        self.nombre_de_point = int(nombre_de_point)
        self.nombre_chiffre_virgule = int(nombre_chiffre_virgule)

def teste(arguments):
    '''
    Cette fonction a pour but d'estimer des temps d'exécution.
    '''
    temp = time.time()
    validate_all_arguments(arguments)
    generate_all_ppm_files(arguments.taille_image, arguments.nombre_de_point,\
                            arguments.nombre_chiffre_virgule)
    generate_gif("out")
    dif = time.time() - temp
    print(f"{arguments.taille_image},{arguments.nombre_de_point},{dif}")

if __name__=="__main__":
    print("taille_image,nombre_de_point,temps")
    image_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tous_nb_points = [1e5, 1e6, 1e7, 1e8]
    for image_size in image_sizes:
        for nb_points in tous_nb_points:
            teste(Arguments(image_size,nb_points, 5))