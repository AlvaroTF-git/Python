print('========= Programa para aprovação de empréstimos bancários ========')
name = str(input('Olá, por favor informe o seu nome completo: '))
money = float(input('Digite aqui o seu salário mensal: '))
house = float(input('Diga o preço da casa na qual deseja comprar: '))
years = int(input('Em quantos anos o senhor pretente pagar a casa? '))
condition = float(money * 0.30)
months = years * 12
prestacao = house / months
if prestacao > condition:
    print('Perdão, infelizmente você não pode financiar a casa!')
elif prestacao < condition:
    print("Parabéns,",name,",Você está apto para financiar a casa!")
else:
    print("Algo ocorreu errado, rode o programa novamente!")





    