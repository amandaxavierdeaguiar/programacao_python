"""Crie um programa que leia uma frase e mostre:
1 - Quantas vezes aparece a letra "A" 
2 - Em que posição aparece a primeira vez
3 - Em que posição aparece a última vez"""

frase_usuario = input("Digite sua frase: ").upper().strip()
quantidade_a = frase_usuario.count("A")
primeiro_a = frase_usuario.find("A") + 1
ultimo_a = (frase_usuario.rfind("A") - frase_usuario.count(" ")) + 1
""" Estou vendo a posição do ultímo A (a partir da direita) e o count está verificando o espaços."""

print(f"Sua Frase aparece {quantidade_a} letras A")
print(f"A primeira letra A que aparece é na {primeiro_a} posição")
print(f"A última letra A que aparece é na {ultimo_a} posição\n\n\n")



"""Crie um programa que leia o primeiro e o ultimo nome da pessoa e exiba as mensagens:
1 - Ola {nome}, o seu registro esta completo
2 - O seu email é {nome}@empresa.pt"""

nome_usuario = input("Digite seu nome completo: ").title().strip()
primeiro_nome = nome_usuario.split()[0]
ultimo_nome = nome_usuario.rsplit()[-1]

print(f"Olá {primeiro_nome} {ultimo_nome}, o seu registro esta completo")
print(f"O seu email é {primeiro_nome.lower()}{ultimo_nome.lower()}@empresa.pt")