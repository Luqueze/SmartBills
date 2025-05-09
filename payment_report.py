"""
MIT License

Copyright (c) 2025 Lucas Felipe Carvalho Caldeira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
(continua...)
"""


import pandas as pd
import streamlit as st

st.title("SmartBill")
st.markdown("After uploading a CSV file, " 
    "it will group the data by title and sum the amounts. " 
    "The results will be displayed in descending order.")

arquivo_csv = st.file_uploader("", type=["csv"])
if st.button("Enter"):

    if arquivo_csv is not None:

        df = pd.read_csv(arquivo_csv)
        # Group by 'title' and sum the values
        df_grouped = df.groupby('title', as_index=False).agg({'date': 'first', 'amount': 'sum'})

        # Sort the data in descending order by the total value of 'amount'.
        df_sorted = df_grouped.sort_values(by='amount', ascending=False)

        # Create a formatted string with spacing.
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
            

        
