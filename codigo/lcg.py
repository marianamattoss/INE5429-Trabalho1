'''
        ================================================
            FEDERAL UNIVERSITY OF SANTA CATARINA
        ================================================
    
    File: ~/codigo/lcg.py
    Created on 4 de abr de 2017 
    @author:  Rodrigo Pedro Marques
    GitHub: https://github.com/rodrigo93/INE5429-Trabalho1
    Professor: Renato Felipe Custodio
 
    This file is part of a college project for the INE5429 Computer Security
    course lectured in Federal University of Santa Catarina.

'''

class LCG(object):
    """
        Linear Congruential Generator e um algoritmo gerador de numeros pseudo-aleatorios.
    """
    
    """
        Construtor da classe.
    """
    def __init__(self):
        return
    
    """
        Formula do algoritmo LCG para gerar os numeros pseudo-aleatorios.
    """
    def gerador(self, semente, m, a, c):
        return (a*semente + c) % (m)
    
    """
        Metodo utilizado para testar o algoritmo LCG.
    """
    def teste(self):
        return self.gerador(74573, m, a, c)
    
    """
        E importante lembrar as regras:
        
        m > 0,
        0 < a < m,
        0 <= c < m,
        0 <= semente < m
    """