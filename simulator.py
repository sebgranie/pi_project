#!/usr/bin/env python3

import random
from math import sqrt
import argparse
import numpy as np

def simulator(n, image = None):
    '''
    Cette fonction retourne une 
    approximation du nombre pi en générant
    des points appartenant ou non à un cercle.
    '''

    compteur = 0
    if image is not None:
        taille = image.shape[0] #return taille des x
        demi_taille = int(taille/2)
    for _ in range(1, n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # print(f"({x},{y})")
        distance = x**2 + y**2
        distance = sqrt(float(distance))
        if float(distance) < 1:
            if image is not None:
                image[int((x+1)*demi_taille)][int((y+1)*demi_taille)] = (0, 0, 255)
            compteur +=1
        else:
            if image is not None:
                image[int((x+1)*demi_taille)][int((y+1)*demi_taille)] = (238, 130, 238)

    return (float(compteur/n)*4)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Approximation de pi")
    parser.add_argument('nombre_de_points', action='store', type=int)

    arguments = parser.parse_args()

    pi = simulator(arguments.nombre_de_points)
    print(pi)