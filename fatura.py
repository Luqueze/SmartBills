import pandas as pd
import streamlit as st

# Carrega o arquivo CSV
st.title("Csv Processing")
arquivo_csv = st.file_uploader("Upload here: ", type=["csv"])

if st.button("Enter"):

    if arquivo_csv is not None:

        df = pd.read_csv(arquivo_csv)
        # Agrupar por 'title' e somar os valores
        df_grouped = df.groupby('title', as_index=False).agg({'date': 'first', 'amount': 'sum'})

        # Ordenar os dados em ordem decrescente pelo valor total de 'amount'
        df_sorted = df_grouped.sort_values(by='amount', ascending=False)

        # Criar string formatada com espaçamento
        espacamento = []
        espacamento.append(f"{'Date'.ljust(15)}{'Title'.ljust(40)}{'Amount'.rjust(15)}")
        espacamento.append("-" * 70)

        df_sorted = df_sorted[df_sorted['title'] != "Pagamento recebido"]

        for index, row in df_sorted.iterrows():
            data = str(row['date']).ljust(15)
            titulo = str(row['title']).ljust(40)
            valor = f"{row['amount']:.2f}".rjust(15)
            espacamento.append(f"{data}{titulo}{valor}")

        st.write("Values Organized in descending order:")
        st.write(df_sorted)

        if (df_sorted["amount"] != 0).any():
            total = df_sorted["amount"].sum()
            st.write(f"Total: {total:.2f}")
            

        
