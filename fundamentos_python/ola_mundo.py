print("Olá Mundo!\n\n\n\n\n")


#Boas Vindas
mensagem = 'Bem vindos\n\n\n\n\n'
print(mensagem.center(30))

#Soma 2 numeros
print('Soma de dois números\n')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b

print(f'O resultado da sua soma é de {soma}\n\n\n\n\n')

#Antecessor || Sucessor
print('Antecessor e Sucessor')
c = int(input('digite um número:'))
antecessor = c - 1
print(f'Seu antecessor é {antecessor}')

d = int(input('digite outro número:'))
sucessor = d + 1
print(f'Seu sucessor é {sucessor}\n\n\n\n\n\n')


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
print(f'O resultado da divisao é: {resto}')


# Crie um programa que leia 5 notas introduzidas pelo utilizador e calcule a média aritmética entre eles:
print('Média\n'.center(30))
nota1 = float(input('Digite a primeiro nota:'))
nota2 = float(input('Digite a segundo nota:'))
nota3 = float(input('Digite a terceiro nota:'))
nota4 = float(input('Digite a quarto nota:'))
nota5 = float(input('Digite a quinto nota:'))

media = ((nota1 + nota2 + nota3 + nota4 + nota5)/5)
print(f'O valor da média é de {media}')

# Calcule a idade do utilizador

ano_nascimento = int(input('Digite seu ano de Nascimento: '))
data_atual = int(input('Digite a data atual: '))
idade = data_atual - ano_nascimento
print(f'Sua idade é de {idade} anos')

""" Crie um programa que pergunte a quantidade de km percorridos por um carro alugado 
e quantidade de dais que foi alugado. 
Apresente o total a pagar sabendo que o carro custa 60€ dia e 0.456€/km"""

quantidade_km = float(input('Quantos km foram percorridos? '))
valor_km = (quantidade_km * 0.456)

quantidade_dias = int(input('Quantos dias alugou? '))
valor_dia = 60
valor_dias = (quantidade_dias * valor_dia)

valor_total_pagar = (valor_km + valor_dias)

print(f'O valor pago em relação a km é de {valor_km} €')
print(f'O valor somado da quantidade de dias é de  {valor_dias} €\n')

print(f'O valor total a pagar é de {valor_total_pagar} €')

