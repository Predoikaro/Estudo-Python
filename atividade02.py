# ===============================================
#      SISTEMA INTELIGENTE DE ESTOQUE
# ===============================================

estoque = {          #dicionario com 5 produtos e suas respectivas quantidades
    "Arroz": 20,
    "Feijão": 15,
    "Macarrão": 12,
    "Café": 8,
    "Açúcar": 10
}

print("=== SISTEMA DE ESTOQUE ===") 
num_produtos = len(estoque)  #retorna a quantidade de produtos no estoque
print(f"Quantidade de produtos no estoque: {num_produtos}")

produto_busca = input("\nDigite o nome do produto que deseja buscar: ") 

if produto_busca in estoque:  #verifica se o produto está no estoque
    print(f"O produto '{produto_busca}' está no estoque com {estoque[produto_busca]} unidades.") #se estiver, retorna a quantidade de unidades disponíveis
else:
    print(f"O produto '{produto_busca}' não está no estoque.")#se não estiver, retorna que o produto não está no estoque


print(f"\nProdutos disponiveis no estoque: {list(estoque.keys())} ") #retorna a lista de produtos disponíveis no estoque

print(f"\nQuantidades disponíveis no estoque: {list(estoque.values())}") #retorna a lista de quantidades disponíveis no estoque

print("\n=== RELATÓRIO DO ESTOQUE ===")

for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")


produto_remover = input("\nDigite o nome do produto que deseja remover do estoque: ")
    
if produto_remover in estoque:  #verifica se o produto está no estoque
        del estoque[produto_remover]  #remove o produto do estoque
        print(f"O produto '{produto_remover}' foi removido do estoque.")

else: 
        print(f"\nO produto '{produto_remover}' não está no estoque.") #se não estiver, retorna que o produto não está no estoque

print(f"\nEstoque atualizado:")
print(estoque)

print(f"\nProdutos disponiveis no estoque: {len(estoque)}") #retorna a lista de produtos disponíveis no estoque



