estoque = {
    "Arroz": 20,
    "Feijão": 15,
    "Macarrão": 12,
    "Café": 8,
    "Açúcar": 10
}

for produto, quantidade in estoque.items():
    print(produto, quantidade)

pedido = input("Qual produto você deseja? ")

if pedido in estoque:
    quantidade_desejada = int(input("Quantos você deseja? "))
    if estoque[pedido] >= quantidade_desejada:              
        estoque[pedido] -= quantidade_desejada
        print(f"Produto: {pedido}, Quantidade: {quantidade_desejada}")
    else:
        print("Quantidade insuficiente em estoque.")
else:
    print("Produto não encontrado.")

print(estoque)


