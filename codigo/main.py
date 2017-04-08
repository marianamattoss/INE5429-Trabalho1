##    @package main
#        ================================================
#            FEDERAL UNIVERSITY OF SANTA CATARINA
#        ================================================
#    
#    File: ~/codigo/main.py
#    Created on 4 de abr de 2017 
#    @author:  Rodrigo Pedro Marques
#    GitHub: https://github.com/rodrigo93/INE5429-Trabalho1
#    Professor: Renato Felipe Custodio
# 
#    This file is part of a college project for the INE5429 Computer Security
#    course lectured in Federal University of Santa Catarina.
import time
from lcg import LCG
from blumblumshub import BBS
from millerrabin import Millerrabin
from fermat import Fermat

##
#    Funcao main que ira gerar os numeros primos
if __name__ == '__main__':
    tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]  #Tamanhos dos numeros que serao gerados pelos geradores
    
    lcg = LCG(74573)            #semente do LCG
    bbs = BBS(88667)            #semente do BBS
    miller = Millerrabin(50)    #50 iteracoes
    fermat = Fermat(50)         #50 iteracoes
    
    print "OK"