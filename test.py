#!/usr/bin/env python3
'''
Ce module m'a permit de réaliser mes tests sur le
programme approximate_pi.py, afin de recueillir des
données que j'ai exploitées dans les modules
complexite_temporelle.py et complexite_spatiale.py.
'''
import time
# from approximate_pi import PiEstimator, validate_all_arguments, generate_all_ppm_files,\
#     generate_ppm_file, color_image_with_points, write_pi_on_image, generate_gif,\
#     create_or_clean_folder, validation_points

from approximate_pi import validate_all_arguments, generate_all_ppm_files, generate_gif

class Arguments:
    '''
    Cette classe permet de récupérer les arguments du programme
    approximate_pi.py et garder la même structure afin de
    pouvoir réaliser les tests depuis ce module annexe.
    '''
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
    print(f"{arguments.taille_image}, {arguments.nombre_de_point}, {dif}")

if __name__ == "__main__":
    print("taille_image,nombre_de_point,temps")
    IMAGE_SIZES = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    TOUS_NB_POINTS = [1e5, 1e6, 1e7, 1e8]
    for image_size in IMAGE_SIZES:
        for nb_points in TOUS_NB_POINTS:
            teste(Arguments(image_size, nb_points, 5))
