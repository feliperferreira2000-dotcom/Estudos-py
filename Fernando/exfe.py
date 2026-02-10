"""
Faça um Script que solicite:
o seu nome
nome da sua mãe
nome do seu pai
sua idade

Deve calcular quantos anos você terá em 3 anos
imprimir na tela exatamente o resultado:
"Eu sou o Felipe, filho do Sergio e da Cecília. Daqui 3 anos eu terei 21 anos"
"""

nome=input("Qual é seu nome?\n").strip()
nm=input("Qual é o nome da sua mãe?\n").strip()
np=input("Qual é o nome do seu pai?").strip()
id=input("Qual a sua idade?\n").strip()
s=int(id)+3

print("Eu sou {}, filho do {} e da {}. Daqui 3 anos eu terei {} anos.".format(nome, np, nm, s))






















































