import sys

# Criando lista vazia (pessoas)
pessoas = []

# Definindo função
"""
- Palavra reservada "def" define uma função
- A seguir vem o nome da função
- Parênteses podem receber parâmetros (opcionais)
- Dois pontos indicam o início do bloco de código da função
- O bloco de código deve ser indentado (4 espaços ou 1 tab)
- A palavra reservada "return" indica o valor de retorno da função (opcional)

def nome_da_funcao():
    # bloco de execução da funçaõ
    return # Pode ou não retornar algo, se não retornar, o valor é 'None'
"""
def pedir_nome():
    nome = input("Qual é o seu nome? ").strip()
    nome = nome.capitalize()
    return nome

def ver_pessoas():
    for pessoa in pessoas:
        print(pessoa)
    else:
        print(f"\n Total de {len(pessoas)} pessoas.")

def adicionar_pessoa_na_lista():
    pessoas.append(pedir_nome())

while True:
    print("1 - Ver pessoas")
    print("2 - Adicionar pessoa")
    print("0 - Sair")

    opcao = input("Selecione uma opção entre [0,1,2]:\n")

    if opcao.isnumeric():
        opcao = int(opcao)
    else:
        pass

    if opcao in [0, 1, 2]:
        if opcao == 0:
            print("Finalizando a execução do programa ...")
            sys.exit()
        elif opcao == 1:
            ver_pessoas()
        elif opcao == 2:
            adicionar_pessoa_na_lista()
    else:
        print("Opção Inválida! Tente novamente", end="\n\n")


