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
    miller = Millerrabin(5)    #5 iteracoes
    fermat = Fermat(5)         #5 iteracoes
    
    outFile = open("numeroPrimos.txt", "wb")
    
    #Testando LCG com Miller
    print "Gerando possiveis numeros primos com LCG e Miller.\n"
    start_lcg_miller_time = time.time()
    outFile.write("Possiveis numeros primos gerados por LCG e Miller: \n")
    for m in tamanhos:
        while True:
            numeroPrimo = lcg.gerador(m, 1103515245, 12345)
            if miller.teste(numeroPrimo):
                outFile.write(str(numeroPrimo) + "\n")
                print "Um possivel numero primo de tamanho ", m, " bits foi gerado em ", (time.time() - start_lcg_miller_time), " segundos."
                break
                
    end_lcg_miller_time = time.time() - start_lcg_miller_time
    tempoDeExecucao = "--- Tempo de execucao: %s segundos. --- \n" % end_lcg_miller_time          
    outFile.write(tempoDeExecucao)
     
    #Testando LCG com Fermat
    print "Gerando possiveis numeros primos com LCG e Fermat.\n"
    start_lcg_fermat_time = time.time()
    outFile.write("Possiveis numeros primos gerados por LCG e Fermat: \n")
    for m in tamanhos:
        while True:
            numeroPrimo = lcg.gerador(m, 1103515245, 12345)
            if fermat.teste(numeroPrimo):
                outFile.write(str(numeroPrimo) + "\n")
                print "Um possivel numero primo de tamanho ", m, " bits foi gerado em ", (time.time() - start_lcg_fermat_time), " segundos."
                break
                
    end_lcg_fermat_time = time.time() - start_lcg_fermat_time
    tempoDeExecucao = "--- Tempo de execucao: %s segundos. --- \n" % end_lcg_fermat_time          
    outFile.write(tempoDeExecucao)            
    
    #Testando BBS com Miller    
    print "Gerando possiveis numeros primos com BBS e Miller.\n"
    start_bbs_miller_time = time.time()
    outFile.write("Possiveis numeros primos gerados por BBS e Miller: \n")
    for m in tamanhos:
        bbs = BBS(74573) 
        while True:
            numeroPrimo = bbs.gerador(m)
            if miller.teste(numeroPrimo):
                outFile.write(str(numeroPrimo) + "\n")
                print "Um possivel numero primo de tamanho ", m, " bits foi gerado em ", (time.time() - start_bbs_miller_time), " segundos."
                break
                
    end_bbs_miller_time = time.time() - start_bbs_miller_time
    tempoDeExecucao = "--- Tempo de execucao: %s segundos. --- \n" % end_bbs_miller_time          
    outFile.write(tempoDeExecucao)      

    #Testando BBS com Fermat
    print "Gerando possiveis numeros primos com BBS e Fermat.\n"
    start_bbs_fermat_time = time.time()
    outFile.write("Possiveis numeros primos gerados por BBS e Fermat: \n")
    for m in tamanhos:
        bbs = BBS(74573) 
        while True:
            numeroPrimo = bbs.gerador(m)
            if fermat.teste(numeroPrimo):
                outFile.write(str(numeroPrimo) + "\n")
                print "Um possivel numero primo de tamanho ", m, " bits foi gerado em ", (time.time() - start_bbs_miller_time), " segundos."
                break
                
    end_bbs_fermat_time = time.time() - start_bbs_fermat_time
    tempoDeExecucao = "--- Tempo de execucao: %s segundos. --- \n" % end_bbs_fermat_time          
    outFile.write(tempoDeExecucao)      
    
    outFile.close()
    
    print "PROGRAMA FINALIZADO COM EXITO"