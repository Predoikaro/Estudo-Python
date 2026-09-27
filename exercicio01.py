nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")    
nota3 = input("Digite a terceira nota: ")
média = (float(nota1) + float(nota2) + float(nota3)) / 3
print(f"A média das notas é: {média:.2f}")
if média >= 7:
    print("Aprovado")
elif média >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    