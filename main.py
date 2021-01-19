# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:03:53 2021

@author: Vivien
"""

import numpy as np
import matplotlib.pyplot as plt

def draw(vect, plt, color): 
    array = np.array([[0, 0, vect[0], vect[1]]])
    X, Y, U, V = zip(*array)
    ax = plt.gca()
    ax.quiver(X, Y, U, V,color=color, angles='xy', scale_units='xy',scale=1)
    plt.draw()

#Configuration du grpahe
plt.figure()
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
ax = plt.gca()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

#Affichage de deux vecteurs de test
draw([4,4], plt, 'b')
draw([1,4], plt, 'r')

#Affichage du graphe
plt.show()