somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres20 = 0
for p in range(1,5):
    print(f'----- {p} -----')
    nome = str(input("Digite seu nome completo: ")).strip()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaidade = idade + somaidade
    mediaidade = somaidade / 4
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 = mulheres20 + 1
print(f'A média da idade do grupo é de: {mediaidade}')
print(f"O nome do homem mais velho é {nomevelho}, com {maioridadehomem}")
print(f"A Idade da mulher mais jovem é de: {mulheres20}")
    
    
