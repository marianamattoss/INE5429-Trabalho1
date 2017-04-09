##	@package millerrabin
#        ================================================
#            FEDERAL UNIVERSITY OF SANTA CATARINA
#        ================================================
#    
#    File: ~/codigo/millerrabin.py
#    Created on 4 de abr de 2017 
#    @author:  Rodrigo Pedro Marques
#    GitHub: https://github.com/rodrigo93/INE5429-Trabalho1
#    Professor: Renato Felipe Custodio
# 
#    This file is part of a college project for the INE5429 Computer Security
#    course lectured in Federal University of Santa Catarina.
import time
import random

##
#    Miller Rabin e um algoritmo para realizar a verificacao da primalidade de um dado numero.
class Millerrabin(object):

    
    ##
    #    Construtor da classe.
    #    @param self ponteiro para o objeto
    #    @param it iteracoes que o algoritmo ira realizar
    def __init__(self, it):
        self.iteracoes = it
        return

    ##
    #	Testa a base 'a' para verificar se 'a' eh um candidato para a composicao de 'numero'
    #	@param self ponteiro para o objeto
    #	@param a numero aleatorio dentro do intervalor 1 <= a <= n-1
    #	@param d valor de d
    #	@param s valor de s
    #	@param numero numero que ira tentar ser decomposto
    def decompoe(self, a, d, s, numero):
        if pow(a, d, numero) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, numero) == numero-1:
                return False
        return True 
 
    ##
    #	Metodo utilizado para testar a primalidade de um numero.
    #	@param self ponteiro para o objeto.
    #	@param numero numero que tera sua primalidade testada.
    def teste(self, numero):
        # Verifica se o numero e par
        if numero % 2 == 0:
            if numero == 2:
                return True
            return False

        # caso num nao seja primo
        # descoberta dos valores de s e d
        s = 0
        d = numero-1
        while True:
            quociente, resto = divmod(d, 2)
            if resto == 1:
                break
            s += 1
            d = quociente
        assert(2**s * d == numero-1)
 
        for it in xrange(self.iteracoes):
            a = random.randrange(2, numero)
            if self.decompoe(a, d, s, numero):
                return False
            
        return True 
        return 

