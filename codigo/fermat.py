## @package fermat
#        ================================================
#            FEDERAL UNIVERSITY OF SANTA CATARINA
#        ================================================
#   
#    File: ~/codigo/fermat.py
#    Created on 4 de abr de 2017 
#    @author:  Rodrigo Pedro Marques
#    GitHub: https://github.com/rodrigo93/INE5429-Trabalho1
#    Professor: Renato Felipe Custodio
# 
#    This file is part of a college project for the INE5429 Computer Security
#    course lectured in Federal University of Santa Catarina.
import random

##
#    Fermat e um algoritmo para realizar a verificacao da primalidade de um dado numero.
#
class Fermat(object):
    
    ##
    #    Construtor da classe.
    #    @param self ponteiro do objeto
    #    @param it numero de iteracoes que serao realizadas
    def __init__(self, it):
        self.iteracoes = it
        return
    
    ##
    #   Formula do algoritmo BBS para gerar os numeros pseudo-aleatorios.
    #   
    def teste(self, numero):
        if numero == 2:
            return True
    
        if numero % 2 == 0:
            return False
    
        for it in xrange(self.iteracoes):
            a = random.randint(1, numero-1)
    
            if pow(a, numero-1) % numero != 1:
                return False
        return True

"""
##
#    Funcao inicial.
#   
if __name__ == '__main__':
    fermat = Fermat(50)
    numero = 88666
    if fermat.teste(numero):
        print "O numero ", numero, " provavelmente eh primo."
    else:
        print "O numero ", numero, " nao eh primo."

"""