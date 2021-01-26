# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:03:53 2021

@author: Vivien
"""


from sympy.abc import x
from sympy.polys.polyerrors import NotInvertible
from sympy import ZZ, Poly
from sympy import GF, invert
import math


class Ntru:

    #Parameters
    
    #Convolution Ring P = Z[X] / (X^N - 1)
    N = 11
    #Must be prime and p << q
    p = 3
    #Must be prime
    q = 61
    
    #Random polynom
    f = None
    g = None
    
    #(X^N - 1)
    r = None
    
    #modular inverse
    f_p = None
    f_q = None
    
    #public key
    h = None

    def __init__(self, N, p, q):
        self.N = N
        self.p = p
        self.q = q
        
        #Random polynom (not generated with code yet ...)
        self.f = Poly(-x**10 - x**8 - x**6 + x**4 + x**2 + x + 1, x).set_domain(ZZ)
        self.g = Poly(-x**9 - x**8 - x**6 + x**4 + x**2 + 1, x).set_domain(ZZ)
        
        #(X^N - 1)  
        self.r = Poly(x ** self.N - 1, x).set_domain(ZZ)
    
        #Debug
        print("f = {}".format(self.f))
        print("g = {}".format(self.g))
        print("r = {}".format(self.r))
    
    def generate_public_key(self):
        #Compute fp and fq
        self.f_p = inv_poly = invert(self.f, self. r, domain=GF(self.p))
        self.f_q = inv_poly = invert(self.f, self.r, domain=GF(self.q))
        
        #Compute public key h = p * g * f_q (mod q)
        self.h = ((self.p * self.f_q * self.g) % self.r).trunc(self.q)
        
        #Debug
        print("Generating public key ...")    
        print("f_p = {}".format(self.f_p))
        print("f_q = {}".format(self.f_q))
        print("h = {}".format(self.h))
        
    def encryption(self, msg):
        #encryption
        #Adding randomness to the encryption
        random_noise = Poly(-x**9 + x**7 + x**4 - x**3 + 1, x)
        #Encryption 
        cypher = Poly(((random_noise*self.h) + msg) % self.r).trunc(self.q)
        #debug
        print("message = {}".format(msg))
        print("cypher = {}".format(cypher))
        
        return cypher
    
    def decryption(self, cypher):
        #decryption
        a = Poly((self.f*cypher) % self.r).trunc(self.q)
        decypher = Poly((self.f_p * a) % self.r).trunc(self.p)
        
        #debug
        print("a = {}".format(a))
        print("m_decypher = {}".format(decypher))
        
        return decypher
    
    def is_prime(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True