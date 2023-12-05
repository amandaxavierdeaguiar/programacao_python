# Crie um programa que leia 5 notas introduzidas pelo utilizador e calcule a média aritmética entre eles:

print('Média\n'.center(30))
nota1 = float(input('Digite a primeiro nota:'))
nota2 = float(input('Digite a segundo nota:'))
nota3 = float(input('Digite a terceiro nota:'))
nota4 = float(input('Digite a quarto nota:'))
nota5 = float(input('Digite a quinto nota:'))

media = ((nota1 + nota2 + nota3 + nota4 + nota5)/5)
print(f'O valor da média é de {media}')

if(media >= 10):
    print("Aprovado")
elif(media >= 8.5):
    print("Em recuperação")
else:
    print("Reprovado")



""" Ex 16 - Crie um programa que leia a média que leia 5 notas de um aluno e calcule a sua média
>= 9.5 passou
> 8 e < 9.5  em recuperacao
<8 reprova
"""

nota = float(input("Digite a nota 1 = "))
nota2 = float(input("Digite a nota 2 = "))
nota3 = float(input("Digite a nota 3 = "))
nota4 = float(input("Digite a nota 4 = "))
nota5 = float(input("Digite a nota 5 = "))

media = ((nota + nota2 + nota3 + nota4 + nota5) / 5)

print(f"A sua média é de {media}")

if media >= 9.5:
    print("Aprovado")
elif media > 8 and media < 9.5:
    print("Em recuperacao")
else:
    print("Reprova")

