#!/usr/bin/env python3
'''
Ce programme est module utilisé par approximate.py. Son objectif
concerne uniquement le calcul d'approximation du nombre π.
'''
import argparse
from math import sqrt
import random

def simulator(points, list_int=None, list_ext=None):
    '''
    Cette fonction retourne une approximation du nombre pi en générant
    aléatoirement des points appartenant ou non à un cercle. Si des
    listes sont renseignées, les coordonnées des points seront
    appartenant au cercle ou
    '''
    if list_int is None:
        list_int = []
    if list_ext is None:
        list_ext = []

    for _ in range(1, points):
        point_x = random.uniform(-1, 1)
        point_y = random.uniform(-1, 1)
        distance = point_x**2 + point_y**2
        distance = sqrt(float(distance))
        if float(distance) < 1.0:
            list_int.append((point_x, point_y))
        else:
            list_ext.append((point_x, point_y))

    return float(len(list_int)/points)*4.0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approximation de pi")
    parser.add_argument('nombre_de_points', action='store', type=int)
    arguments = parser.parse_args()
    pi_val = simulator(arguments.nombre_de_points)
