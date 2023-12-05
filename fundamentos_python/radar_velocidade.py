"""Ex14 - Crie um programa que leia um número inteiro introduzido pelo utilizadfor e que simule um radar de velocidade.
  > 80 km/h multado 
  <= 80km/h não multado """

velocidade = int(input("Digite a Quilometragem: "))
velocidade_acima = (velocidade - 80) * 7
total = velocidade_acima + 100

if velocidade > 80:
    print('Velocidade acima do permitido!')
    print(f'Recebeu a multa de {total} €\n100€ da multa e {velocidade_acima}€ por cada km acima do permitido. \n')
else:
    print('Não receberá multa.')

""" Ex 15 Crie um programa que leia um número inteiro e mostre se é par ou ímpar """

"""numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Seu número é PAR ')
else:
    print('Seu número é IMPAR')"""