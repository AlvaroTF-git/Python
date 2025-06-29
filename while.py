print("Escolha dois números entre 0 e 10.")
primeiro = int(input('Escolha o primeiro: '))
segundo = int(input('Escolha o segundo: '))
opcao = 0
sair = 5
while opcao != sair:
    print("=-=-=-==-=-=-=")
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    print("=-=-=-==-=-=-=")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print(primeiro + segundo)
    if opcao == 2:
        print(primeiro * segundo)
    if opcao == 3:
        if primeiro > segundo:
            print(f'O número {primeiro} é maior do que o número {segundo}!')
        else:
            print(f'O número {segundo} é maior do que o número {primeiro}!')
    if opcao == 4:
        primeiro = int(input('Escolha o primeiro número: '))
        segundo = int(input('Escolha o segundo número: '))
print('Saindo!!!')
