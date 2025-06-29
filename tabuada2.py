print("Tabuada de vários números")
tabuada = 1
numeros = 0
while True:
    tabuada = int(input('Digite um número para ver a tabuada dele: '))
    if tabuada < 0:
        break
    for numeros in range(0, 11, +1):
        print(f"{tabuada} x {numeros} = {tabuada * numeros}")
print("Saindo do programa...")
