nome = "Fernando"
idade = int(input("idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 21:
    print("Você é maior de idade no Brasil, e menor no USA.")
elif idade >= 21:
    print("Você é maior de idade")

