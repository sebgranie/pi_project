#!/usr/bin/env python3.7
'''
pi
'''
import argparse
from math import sqrt
import random

def simulator(points, image = None):
    '''
    Cette fonction retourne une
    approximation du nombre pi en générant
    des points appartenant ou non à un cercle.
    '''
    compteur = 0
    if image is not None:
        taille = image.shape[0] #return taille des x
        demi_taille = int(taille/2)
    for _ in range(1, points):
        point_x = random.uniform(-1, 1)
        point_y = random.uniform(-1, 1)
        # print(f"({x},{y})")
        distance = point_x**2 + point_y**2
        distance = sqrt(float(distance))
        if float(distance) < 1:
            if image is not None:
                image[int((point_x+1)*demi_taille)]\
                     [int((point_y+1)*demi_taille)] = (0, 0, 255)
            compteur +=1
        else:
            if image is not None:
                image[int((point_x+1)*demi_taille)]\
                     [int((point_y+1)*demi_taille)] = (238, 130, 238)
    return float(compteur/points)*4

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approximation de pi")
    parser.add_argument('nombre_de_points', action='store', type=int)
    arguments = parser.parse_args()
    pi = simulator(arguments.nombre_de_points)
    print(pi)
