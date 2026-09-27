numero = int(input("Digite um número: "))

soma = 0
pares = 0
impares = 0

for i in range(1, numero + 1):

    soma = soma + i

    if i % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Soma: {soma}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")