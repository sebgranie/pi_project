#!/usr/bin/env python3
'''
Ce programme est module utilisé par approximate.py.
Son objectif concerne uniquement le calcul d'approximation
du nombre π en se basant sur la méthode de Monte-Carlo.
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

    for _ in range(points):
        point_x = random.uniform(-1.0, 1.0)
        point_y = random.uniform(-1.0, 1.0)
        distance = point_x**2 + point_y**2
        distance = sqrt(float(distance))
        if distance < 1.0:
            list_int.append((point_x, point_y))
        else:
            list_ext.append((point_x, point_y))
    return (float(len(list_int))/float(points))*4.0

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Approximation de pi")
    PARSER.add_argument('nombre_de_points', action='store', type=int)
    ARGUMENTS = PARSER.parse_args()
    PI_VAL = simulator(ARGUMENTS.nombre_de_points)
    print(PI_VAL)
