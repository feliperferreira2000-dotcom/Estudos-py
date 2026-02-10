    #1 Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado

nome=input('Qual é seu nome?')
print(f'Olá, {nome}. Prazer em te conhecer!') #Errei algo. Correção: Esqueci do f

    #2 Crie um script que leia o dia, mes e o ano de nascimento de uma pessoa e mostra uma mensagem com data formada

dia=input('Dia=')       
mes=input('mes=')
ano=input('ano=')   

print(f'Voce nasceu no dia {dia}, de {mes} de {ano}. Correto?') #Errei. Correção: Não havia colocado o f!

    #3 Crie um script python que leia dois numeros e tente mostra a soma entre eles 
    
n1=int(input('Digite um númro:')) 
n2=int(input('Digite mais um númro:'))
s=n1+n2 
print('A soma vale',s)

    #4 Crie um programa que leia dois numeros e mostra a soma entre eles 

n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
s= n1+n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

   #5 Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

n1=int(input("Digite um numero: "))
S=n1+1
A=n1-1
print("O sucessor de {} é {}, e seu antecessor é {}".format(n1, S, A))

    #6 Crie um algoritmo que leia um número e mostre o dobro, triplo e raiz quadradra

n1=int(input("Digite um valor: "))
d=n1*2
t=n1*3
r=n1*(1/2)
print("O dobro de {} é igual a {}, o triplo é {}, e sua raiz é {}.".format(n1, d, t, r))

    #7  Desenvolva um prograga que leia as duas notas de um aluno, calcule e mostre sua media

n1=int(input("Nota 1: "))
n2=int(input("Nota 2: "))
m=(n1+n2)/2
print("Um aluno tirou em suas provas {} e {}. Logo sua média foi {}!".format(n1, n2, m))

    #8 Escreva um programa que leia um valor em metros e o exiba convertido e centimetros e milimetros 

n1=int(input("Digite um valor: "))
c=n1*100
m=n1*1000
print("O valor citado é igual a {}m, {}cm , e {}mm.".format(n1, c, m))

    #9 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n1=int(input("Me fale um valor: ")) 
v1=n1*1  
v2=n1*2
v3=n1*3
v4=n1*4
v5=n1*5
v6=n1*6
v7=n1*7
v8=n1*8
v9=n1*9
v10=n1*10

print("A tabuada do número {} é igual a: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(n1, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10))
