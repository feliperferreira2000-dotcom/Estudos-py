print("Olá Mundo") 

# Definindo variaveis nome e idade
nome="Felipe"
idade=18

#print(f"{nome},{idade}")
print(f"Olá sou {nome},Tenho {idade} anos.")
#print(type(nome))
#print(type(idade))

# Definindo uma função
def imprimir_nome():
    pass
    print(f"/// {nome}")
    return nome,idade

# Executando uma função 
print(imprimir_nome)
nome2=(imprimir_nome())
print(nome2)
print(nome2[0])
print(nome2[1])
#print(nome2[2]) Aqui da erro de acesso de indice: IndexError












