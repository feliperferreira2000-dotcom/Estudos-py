#Introdução
    
print('Olá, mundo!')
print(7+4)
print('7'+'4')
 
#Variáveis

nome='Felipe'
idade=18
peso=107

print(nome,idade,peso)
                #Coloquei vírgulas pois a valores e mensagens na frase, nesse caso não pode usar o mais. 

nome=input('Qual é seu nome?')
idade=input('Qual a sua idade?')
peso=input('Qual o seu peso?')

#Tipos primitivos

n1=int(input('Digite um valor:'))               #Sem o int ele não soma, ele apenas junta!!!!
n2=int(input('Digite outro: '))
s= n1+n2
print('A soma entre', n1,'e', n2 , 'vale', s)                   #Maneira 1 (Sintax Antiga)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))           #Maneira 2 (SIntax Nova)

n=float(input('Digite um valor: '))     #Mostra o numero inteiro so que com . ex: 4.0 
print(n)

n=bool(input('Digite um valor: '))     #Te, Valor Dentro Vai ser True, caso contrario vai ser False
print((n))

n=(input('Digite um valor: '))         #Esse comando me diz se é possivel converter o valor em numero com o tipo primitivo int 
print(n.isnumeric())

n=(input('Digite um valor: '))         #Igual o de cima só que para letra
print(n.isalpha())

n=(input('Digite um valor: '))         #Para ambos (Numeros e letras)
print(n.isalnum())

n=(input('Digite um valor: '))         #Me fala se o valor esta apenas em letras maiusculas
print(n.isupper())

dia=input('Dia=')
mes=input('mes=')
ano=input('ano=') 
aa=int(input("Qual o ano atual?"))
idade=aa-int(ano)


print(f'Voce nasceu no dia {dia}, de {mes} de {ano}. Correto?')


print("Sua idade é",idade )

#Módulos 

from math import sqrt, floor            #Importa a função de raiz quadrada de um numero, e caso o numero tiver casas depois da virgula arredonda para baixo
num = int(input("Digite um numero:"))
raiz = sqrt(num)
print("A raiz de {} é igual a {}".format(num, floor(raiz))) 

import random           #Para Gerar um numero aleatorio
num = random.random()
print(num) 

import random                   #Gera um número inteiro de um até 10
num = random.randint(1, 10)
print(num)

 





























































