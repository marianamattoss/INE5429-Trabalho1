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

##
#    Miller Rabin e um algoritmo para realizar a verificacao da primalidade de um dado numero.
class Millerrabin(object):

    
    ##
    #   Construtor da classe.
	#	@param self ponteiro para o objeto
    def __init__(self):
		self.tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
        return

	##
	#	Tenta decompor um numero
	#	@param self ponteiro para o objeto
	#	@param a
	#	@param d
	#	@param s
	#	@param numero numero que ira tentar ser decomposto
    def decompoe(self, a, d, s, numero):
        if (a**d % numero) == 1:
            return False
        for i in range(s):
            if (a**(2**i * d) % numero) == numero-1:
                return False
        return True 
 
	##
	#	Metodo utilizado para testar a primalidade de um numero.
	#	@param self ponteiro para o objeto.
	#	@param numero numero que tera sua primalidade testada.
    def teste(self, numero):
        # Verifica se o numero e par
        if num % 2 == 0:
            if num == 2:
                return True
            return False

        # caso num não seja primo
        # descoberta dos valores de s e d
        s = 0
        d = num-1
        while True:
            quociente, resto = divmod(d, 2)
            if resto == 1:
                break
            s += 1
            d = quociente
        assert(2**s * d == numero-1)
 
        for i in range(self.i):
            a = random.randrange(2, numero)
            if self.decompoe(a, d, s, numero):
                return False
 
        return True 
        return 

##
#	Funcao inicial.
if __name__ == '__main__':
    start_time = time.time()
    rabin = Millerrabin()
    rabin.teste()
    print("--- Tempo de execucao: %s segundos ---" % (time.time() - start_time))
