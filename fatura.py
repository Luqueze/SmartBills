import pandas as pd

# Carrega e ordena
arquivo_csv = "C:/pablo/fatura04.csv"
df = pd.read_csv(arquivo_csv)

# Ordenar
df_sorted = df.sort_values(by='amount', ascending=False)

# Criar string formatada com espaçamento
espacamento = []
espacamento.append(f"{'Date'.ljust(15)}{'Title'.ljust(40)}{'Amount'.rjust(15)}")
espacamento.append("-" * 70)

for index, row in df_sorted.iterrows():
    data = str(row['date']).ljust(15)
    titulo = str(row['title']).ljust(40)
    valor = f"{row['amount']:.2f}".rjust(15)
    espacamento.append(f"{data}{titulo}{valor}")

# Salvar como um arquivo .txt "formatado"
with open("relatorio_formatado.txt", "w", encoding="utf-8") as f:
    for linha in espacamento:
        f.write(linha + "\n")

print("Relatório formatado salvo como 'relatorio_formatado.txt'")
