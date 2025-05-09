import pandas as pd

# Carrega o arquivo CSV
arquivo_csv = "C:/pablo/fatura04.csv"
df = pd.read_csv(arquivo_csv)

# Conta quantas vezes cada título aparece
title_counts = df['title'].value_counts()

# Agrupa por 'title' e soma os valores
df_grouped = df.groupby('title', as_index=False).agg({'date': 'first', 'amount': 'sum'})

# Adiciona a contagem ao DataFrame agrupado
df_grouped['count'] = df_grouped['title'].map(title_counts)

# Remove a data se o título aparece mais de uma vez
df_grouped['date'] = df_grouped.apply(lambda row: '' if row['count'] > 1 else row['date'], axis=1)

# Ordenar os dados em ordem decrescente pelo valor total de 'amount'
df_sorted = df_grouped.sort_values(by='amount', ascending=False)

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
