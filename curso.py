#ATIVIDADE 01

n1 = float(input("Qual a primeira nota: "))
n2 = float(input("Qual a segunda nota: "))

média = (n1 + n2)/2

if média >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#ATIVIDADE 02 = TRIANGULO

base = float(input("Qual a base do triângulo: "))
altura = float(input("Qual a altura do triângulo: "))

area = (base*altura)/2

print(f"O resultado da area do triangulo: {area}")

#ATIVIDADE 03 = CONVERSOR DE SEGUNDOS

segundos = int(input("Digite o número de segundos: "))
horas = segundos // 3600
minutos = segundos // 60

print(f"Horas: {horas}\n Minutos: {minutos}")

#ATIVIDADE 04 = JUROS SIMPLES

print('Informe os dados para o cálculo dos juros')
capital = float(input('Capital: '))
taxa = float(input('Taxa de juros: '))
tempo = float(input('Tempo: '))
juros = capital * taxa * tempo / 100
print(f"O valor dos juros é: {juros}")