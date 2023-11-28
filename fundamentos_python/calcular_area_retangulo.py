#import biblioteca
import math

#definicao de funcao
def calcular_area_retanguo(largura, altura):
    """"Calcula a área de um retângulo"""
    return largura * altura

#codigo principal
#definir as dimensões do retângulo
largura = 5
altura = 3

#chamando a funcao para calcular a área
area = calcular_area_retanguo(largura, altura)

#imprimindo o resultado
print(f"A área do retângulo é {area}")
