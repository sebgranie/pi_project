#!/usr/bin/env python3
'''
Ce programme permet d'afficher un graphique évaluant la complexité temporelle
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
Y = np.array([100000, 1000000, 10000000, 100000000])
Z = np.array([[0.44110894203186035, 2.5205373764038086, 19.39069938659668, 193.6669201850891],
              [0.4694180488586426, 2.4512555599212646, 21.18052625656128, 204.19957876205444],
              [0.7208893299102783, 2.6152734756469727, 20.83769726753235, 204.18992233276367],
              [0.775820255279541, 2.967527389526367, 22.093643188476562, 209.77208948135376],
              [0.9615116119384766, 2.8182806968688965, 23.471038579940796, 212.96404027938843],
              [1.3253424167633057, 3.039436101913452, 20.08140778541565, 202.26704478263855],
              [1.3413631916046143, 3.4942314624786377, 23.537698984146118, 207.69750547409058],
              [1.6243116855621338, 3.5182063579559326, 20.867828369140625, 207.94831657409668],
              [1.7966983318328857, 3.8180739879608154, 21.142998695373535, 209.590026140213],
              [2.736236333847046, 4.525357246398926, 23.780110120773315, 213.54226541519165]])

# Création de la grille
XX, YY = np.meshgrid(X, Y)
A = (9 - XX - YY) / 2

# Légende des axes du graphique
AX.set_xlabel("Taille de la l'image (pixel)")
AX.set_ylabel('Nombre de points')
AX.set_zlabel("Temps d'exécution (s)")

# Permet d'obtenir une toile <=> surface comme figure d'affichage
AX.plot_surface(XX, YY, Z.transpose(), alpha=0.75)

plt.title("Complexité temporelle de approximate_pi.py et de ses modules")

# Affiche la figure
plt.show()
