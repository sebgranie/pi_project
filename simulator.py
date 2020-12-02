#!/usr/bin/env python3
'''
Ce programme est module utilisé par approximate.py. Son objectif
concerne uniquement le calcul d'approximation du nombre π.
'''
import argparse
from math import sqrt
import random

def simulator(points, image=None):
    '''
    Cette fonction retourne une approximation du nombre pi
    en générant aléatoirement des points appartenant ou non
    à un cercle. Si une image est passée en argument, nous
    représentons les points aléatoires appartenant au cercle
    à l'aide d'une couleur spécifique. Cette fonction
    renvoie une estimation de la valeur de pi.
    '''
    compteur = 0
    if image is not None:
        taille = image.shape[0]
        demi_taille = int(taille/2)
    for _ in range(1, points):
        point_x = random.uniform(-1, 1)
        point_y = random.uniform(-1, 1)
        distance = point_x**2 + point_y**2
        distance = sqrt(float(distance))
        if float(distance) < 1.0:
            if image is not None:
                # On ajoute 1 aux coordonnées x et y pour
                # obtenir des valeurs de pixels positives
                image[int((point_x+1)*demi_taille)]\
                    [int((point_y+1)*demi_taille)] = (0, 0, 255)
            compteur += 1
        else:
            if image is not None:
                image[int((point_x+1)*demi_taille)]\
                    [int((point_y+1)*demi_taille)] = (238, 130, 238)
    # print(float(compteur/points)*4.0)
    return float(compteur/points)*4.0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approximation de pi")
    parser.add_argument('nombre_de_points', action='store', type=int)
    arguments = parser.parse_args()
    pi_val = simulator(arguments.nombre_de_points)
