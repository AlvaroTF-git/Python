import random
tentativas = 1
cpu = random.randint(1, 10)
jogador = int(1)
while jogador != cpu:
    print("----- Tente adivinhar o número que o computador escolheu -----")
    jogador = int(input('Escolha um número de 1 a 10: '))
    if jogador == cpu:
        print(f"Parabéns, você acertou com um total de {tentativas} tentativas.")
    else:
        print('Infelizmente você errou, tente novamente!')
        tentativas = tentativas + 1
