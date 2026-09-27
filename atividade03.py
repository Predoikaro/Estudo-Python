print("=" * 45)
print("  SELEÇÃO PARA O PROJETO DE TECNOLOGIA")
print("=" * 45)

conhecimentos_exigidos = { # Dados definidos pela instituição
    "python",
    "lógica",
    "git",
    "banco de dados",
    "html"
}

turnos_disponiveis = ("manhã", "tarde") 

# Coleta de dados 
nome = input("\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite seu curso: ")
semestre = int(input("Digite o semestre: "))
email = input("Digite seu email: ")

if "@" in email and "." in email:
    print("Email válido.")
else:
    print("Email inválido.")

conhecimentos_candidato = input(
    "\nInforme seus conhecimentos separados por vírgula: "
)
conhecimentos_candidato = {
    conhecimento.strip().lower()
    for conhecimento in conhecimentos_candidato.split(",")
}

turnos_candidato = input("Qual seu turno disponivel? ")
trabalho_equipe = input("Aceita trabalhar em equipe? ").lower() == "sim"

computador_proprio = input("Você possui computador proprio? ").lower() == "sim"

print("=" * 45)
print("  RESULTADO DA SELEÇÃO")
print("=" * 45)

conhecimentos_compativeis = conhecimentos_candidato.intersection(
    conhecimentos_exigidos
)

conhecimentos_faltantes = conhecimentos_exigidos.difference(
    conhecimentos_candidato
)

pontuacao = len(conhecimentos_compativeis) * 2 

motivos_reprovacao = []

if conhecimentos_faltantes:
    motivos_reprovacao.append(
        f"Conhecimentos faltantes: {conhecimentos_faltantes}"
    )

if turnos_candidato not in turnos_disponiveis:
    motivos_reprovacao.append("Turno inválido.")

if "@" not in email or "." not in email:
    motivos_reprovacao.append("E-mail inválido.")

if not trabalho_equipe:
    motivos_reprovacao.append("Não aceita trabalhar em equipe.")

if not computador_proprio:
    motivos_reprovacao.append("Não possui computador próprio.")

if turnos_candidato in turnos_disponiveis:
    pontuacao += 1

if trabalho_equipe:
    pontuacao += 2

if computador_proprio:
    pontuacao += 1


if pontuacao >5:
    classificacao = "APROVADO"
    motivo = "Cumpriu todas as condições obrigatórias."

elif pontuacao == 5:
    classificacao = "BANCO DE TALENTOS"
    motivo = "Obteve pelo menos 5 pontos."

else:
    classificacao = "NÃO APROVADO"
    motivo = "Obteve menos de 5 pontos."

candidato = {
    "nome": nome,
    "idade": idade,
    "curso": curso,
    "semestre": semestre,
    "email": email,
    "turno": turnos_candidato,
    "trabalho em equipe": trabalho_equipe,
    "computador proprio": computador_proprio,
    "conhecimentos": set(conhecimentos_candidato),
    "compativeis": conhecimentos_compativeis,
    "faltantes": conhecimentos_faltantes,
    "pontuacao": pontuacao,
    "classificacao": classificacao,
    "motivo": motivo
}


print(f"\nnome: {nome} ")
print(f"curso: {curso}")
print(f"turno valido: {turnos_candidato}")
print(f"Trabalho em equipe: {trabalho_equipe}")
print(f"Possui computador: {computador_proprio}")
print(f"conhecimentos compativeis: {conhecimentos_compativeis}")
print(f"Quantidade de conhecimentos compatíveis: {len(conhecimentos_compativeis)}")
print(f"conhecimentos faltantes: {conhecimentos_faltantes}")
print(f"pontuacao: {pontuacao}")
print(f"\n classificacao: {classificacao}")
print(f"motivo: {motivo}")

if motivos_reprovacao:
    print("\nMotivos da reprovação:")
    for motivo_reprovacao in motivos_reprovacao:
        print(f"- {motivo_reprovacao}")