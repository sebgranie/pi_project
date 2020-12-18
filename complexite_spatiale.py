#!/usr/bin/env python3
'''
Ce programme permet d'afficher un graphique évaluant la complexité spatiale
de mon programme. Les données utilisées dans ce module ont été récupérées en
effectuant des tests sur mon programme  approximate_pi.py. Lors de ces tests,
j'ai choisis d'utiliser  différentes tailles d'image (entre 100 et 1000 pixels
de côté) ainsi que des nombres de tirages de points différents (entre 1e5 et 1e8).
'''
import numpy as np
import matplotlib.pyplot as plt

FIG = plt.figure()

AX = FIG.add_subplot(111, projection='3d')

# Valeurs sur les axes
X = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
Y = np.array([100000, 1000000, 10000000])
Z = np.array([[59.376, 69.000, 196.468],
              [59.452, 70.204, 193.356],
              [59.912, 71.076, 197.028],
              [60.632, 71.316, 195.884],
              [61.152, 73.120, 196.464],
              [61.564, 74.260, 196.400],
              [62.536, 75.020, 200.012],
              [72.720, 77.016, 200.684],
              [89.124, 89.164, 201.476],
              [108.088, 107.896, 204.160]])

# Création de la grille
XX, YY = np.meshgrid(X, Y)
A = (9 - XX - YY) / 2

# Légende des axes du graphique
AX.set_xlabel("Taille de la l'image (pixel)")
AX.set_ylabel('Nombre de points')
AX.set_zlabel("Nombre de Mega octets(s)")

# Permet d'obtenir une toile <=> surface comme figure d'affichage
AX.plot_surface(XX, YY, Z.transpose(), alpha=0.75)

plt.title("Complexité spatiale de approximate_pi.py et de ses modules")

# Affiche la figure
plt.show()
