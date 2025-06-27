mediaidade = 0
oldman = 0
oldmanN = 'a'
for p in range(1, 5):
    print(f"==== {p} ====")
    nome = str(input("Digite seu nome completo: ")).strip
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip
    mediaidade = mediaidade + idade
    if p == 1 and sexo in 'Mm':
        oldman = idade
        oldmanN = nome
print(f"oldman")
print(f"oldmanN")