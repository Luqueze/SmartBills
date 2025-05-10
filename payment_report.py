"""
MIT License

Copyright (c) 2025 LUCAS FELIPE CARVALHO CALDEIRA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
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

        df_sorted = df_sorted[df_sorted['title'] != "Pagamento recebido"] 

        st.write("Values Organized in descending order:")
        st.write(df_sorted)

        if (df_sorted["amount"] != 0).any():
            total = df_sorted["amount"].sum()
            st.write(f"Total: {total:.2f}")
            

        
