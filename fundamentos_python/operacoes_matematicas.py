#Cria um programa que leia dois valores introduzidos e que apresente a sua SOMA, SUBTRACAO, MULTIPLICACAO E RESTO

print('Operacoes Matemáticas\n'.center(30))
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

print(f'O resultado da soma é: {soma}')
print(f'O resultado da subtracao é: {subtracao}')
print(f'O resultado da multiplicacao é: {multiplicacao}')
print(f'O resultado da divisao é: {divisao}')
print(f'O resto da divisao é: {resto}')

"""Crie um programa que lê um numero de 0 a 9999 e mostre cada um dos dígitos separados
Ex: 1992 
unidade: 2, dezena: 9, centena: 9 , milhar:1 """

numero = int(input("Digite um número inteiro de  de 0 a 9999: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
