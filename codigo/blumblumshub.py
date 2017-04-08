##	@package blumblumshub
#        ================================================
#            FEDERAL UNIVERSITY OF SANTA CATARINA
#        ================================================
#    
#    File: ~/codigo/blumblumshub.py
#    Created on 4 de abr de 2017 
#    @author:  Rodrigo Pedro Marques
#    GitHub: https://github.com/rodrigo93/INE5429-Trabalho1
#    Professor: Renato Felipe Custodio
# 
#    This file is part of a college project for the INE5429 Computer Security
#    course lectured in Federal University of Santa Catarina.
import time

##
#	Blum Blum Shub e um algoritmo gerador de numeros pseudo-aleatorios.
class BBS(object):

    
	##
	#	Construtor da classe.
	#	@param self ponteiro para o objeto.
	#	@param semente valor que sera atribuido a semente do algoritmo.
    def __init__(self, semente):
        self.seed = semente
        return
    
	##
	#	Formula do algoritmo BBS para gerar os numeros pseudo-aleatorios.
	#	@param self ponteiro do objeto
	#	@param m valor do modulo que ira limitar o tamanho do numero gerado
	#	@return	numero pseudo-aleatorio gerado
    def gerador(self, m):
        self.seed = (self.seed**2) % (2**m)
        return self.seed
    
	##
	#	Metodo utilizado para testar o algoritmo Blum Blum Shub.
	#	@param self ponteiro para o objeto
    def teste(self):
        outFile = open("bbs_output.txt", "wb")
        
        tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
        tabelaDeResultado = []
        indice = 0;
        for m in tamanhos:
            indice += 1
            tabelaDeResultado.append(self.gerador(m))
            print "Para o tamanho m = ", m, " gerou-se o numero ", tabelaDeResultado[indice-1]
            outFile.write(str(tabelaDeResultado[indice-1]) + "\n")
        
        outFile.close()
        return 
"""
##
#	Funcao inicial    
if __name__ == '__main__':
    start_time = time.time()
    bbs = BBS(88667)
    bbs.teste()
    print("--- Tempo de execucao: %s segundos ---" % (time.time() - start_time))
    
    Tempos de execucao:
    --- Tempo de execucao: 0.000319957733154 segundos ---
    --- Tempo de execucao: 0.000370025634766 segundos ---
    --- Tempo de execucao: 0.000658988952637 segundos ---
    --- Tempo de execucao: 0.000383853912354 segundos ---
    --- Tempo de execucao: 0.000336885452271 segundos ---
    
"""