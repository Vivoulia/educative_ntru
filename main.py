# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:45:35 2021

@author: Vivien
"""

from ntru import Ntru
from sympy import ZZ, Poly
from sympy.abc import x

def main():
    
    N = 11
    p = 3
    q = 61
    ntru = Ntru(N, p, q)
    
    #Message 
    m = Poly(x**7 - x**4 + x**3 + x + 1, x).set_domain(ZZ)
    
    ntru.generate_public_key()
    cypher = ntru.encryption(m)
    decypher = ntru.decryption(cypher)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
