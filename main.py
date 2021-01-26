# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:03:53 2021

@author: Vivien
"""

import numpy as np
import numpy.polynomial.polynomial as nppol
import matplotlib.pyplot as plt
from sympy.abc import x
from sympy.polys.polyerrors import NotInvertible
from sympy import ZZ, Poly
from sympy import GF, invert
import math

def draw(vect, plt, color): 
    array = np.array([[0, 0, vect[0], vect[1]]])
    X, Y, U, V = zip(*array)
    ax = plt.gca()
    ax.quiver(X, Y, U, V,color=color, angles='xy', scale_units='xy',scale=1)
    plt.draw()
    
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_2_power(n):
    return n != 0 and (n & (n - 1) == 0)
    
def invert_poly(f_poly, R_poly, p):
    inv_poly = None
    if is_prime(p):
        print("Inverting as p={} is prime".format(p))
        inv_poly = invert(f_poly, R_poly, domain=GF(p))
    else:
        raise Exception("Cannot invert polynomial in Z_{}".format(p))
    #print("Inversion: {}".format(inv_poly))
    return inv_poly



    
#Parameters
N = 11 #Convolution Ring P = Z[X] / (X^N - 1)
p = 3
q = 61

#Random polynom
f = Poly(-x**10 - x**8 - x**6 + x**4 + x**2 + x + 1, x).set_domain(ZZ)
g = Poly(-x**9 - x**8 - x**6 + x**4 + x**2 + 1, x).set_domain(ZZ)
r = Poly(x ** N - 1, x).set_domain(ZZ)

print("f = {}".format(f))
print("g = {}".format(g))
print("r = {}".format(r))

#Compute fp and fq
f_p = invert_poly(f, r, p)
f_q = invert_poly(f, r, q)

f_verif = Poly(x**9 + x**7 + x**5 +2*x**4+2*x**3+2*x**2+x)

print("f_p = {}".format(f_p))
print("f_q = {}".format(f_q))

#Compute public key h = p * g * f_q (mod q)
h = ((p * f_q * g) % r).trunc(q)
print("h = {}".format(h))

#encryption
m = Poly(x**7 - x**4 + x**3 + x + 1, x).set_domain(ZZ)
random_noise = Poly(-x**9 + x**7 + x**4 - x**3 + 1, x)
cypher = Poly(((random_noise*h) + m) % r).trunc(q)
print("cypher = {}".format(cypher))

#decryption
a = Poly((f*cypher) % r).trunc(q)
print("a = {}".format(a))
decypher = Poly((f_p * a) % r).trunc(p)
print("m = {}".format(m))
print("m_decypher = {}".format(decypher))


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