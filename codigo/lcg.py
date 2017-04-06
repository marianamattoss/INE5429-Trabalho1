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
import time

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
        return (a*semente + c) % (2**m)
    
    """
        Metodo utilizado para testar o algoritmo LCG.
        Como exemplo, utilizei os valores:
        semente = 74573,
        m =  aos tamanhos especificados no enunciado
        a =
        c = 
    """
    def teste(self):
        outFile = open("lgc_output.txt", "wb")
        
        tamanhos = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
        tabelaDeResultado = []
        indice = 0;
        for m in tamanhos:
            indice += 1
            tabelaDeResultado.append(self.gerador(16807, m, 1103515245, 12345))
            print "Para o tamanho m = ", m, " gerou-se o numero ", tabelaDeResultado[indice-1]
            outFile.write(str(tabelaDeResultado[indice-1]) + "\n")
        
        outFile.close()
        return

    """
        Eh importante lembrar as regras:
        
        m > 0, modulo,
        0 < a < m, multiplicador, 
        0 <= c < m, incrementador,
        0 <= semente < m, valor inicial
        
        Para o LCG ser um "mixed generator" deve-se respeitar as seguintes regras:
        'm' e 'c' sao relativamente primos;
        'a-1' eh divisivel por todos os fatores primos de 'm';
        'a-1' eh divisivel por 4 se o 'm' tambem for
    """
    
"""
    Funcao inicial
"""    
if __name__ == '__main__':
    start_time = time.time()
    lcg = LCG()
    lcg.teste()
    print("--- Tempo de execucao: %s segundos ---" % (time.time() - start_time))
    
    
    