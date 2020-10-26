#!/usr/bin/env python3

import simulator

def generate_ppm_file(taille, nb_points, decimale):
    couleurs = ["blue", "purple"]
    






if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="generation image")
    parser.add_argument('taille_image', action='store', type=int)
    parser.add_argument('nombre_de_point', action='store', type=int)
    parser.add_argument('nombre_chiffre_virgule', action='store', type=int)

    
    arguments = parser.parse_args()

    generate_ppm_file(arguments.taille_image, arguments.nombre_de_point, arguments.nombre_chiffre_virgule)
