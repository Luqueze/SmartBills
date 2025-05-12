import pandas as pd
import streamlit as st
import os
import plotly.express as px
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("SmartBill")
st.markdown("After uploading a CSV file, it will group the data by title and sum the amounts. The results will be displayed in descending order.")

csv_file = st.file_uploader("", type=["csv"])

if st.button("Enter") and csv_file is not None:
    df = pd.read_csv(csv_file)

    # Group by title and sum amounts
    df_grouped = df.groupby('title', as_index=False).agg({'date': 'first', 'amount': 'sum'})
    df_grouped = df_grouped[df_grouped['amount'] >= 0]
    df_sorted = df_grouped.sort_values(by='amount', ascending=False)

    # API prompt
    items = "\n".join(
        [f"{i+1}. Title: {row['title']} | Amount: {row['amount']}" for i, row in df_sorted.iterrows()]
    )
    prompt = (
        "Classify the following list of financial transactions into appropriate categories. "
        "Return only a list of categories in order, one per line, corresponding to each item.\n\n"
        "Categories are limited to Food, Transport, Subscription, Shopping, Health, Tax, Entertainment. "
        "If amount is less than 0, it is a Refund.\n\n"
        f"{items}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a financial assistant that categorizes expenses."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )

        raw_categories = response.choices[0].message.content.strip().split("\n")
        categories = [cat.strip("- ").strip() for cat in raw_categories]

        # Ensure the number of categories matches the number of rows
        num_rows = len(df_sorted)
        if len(categories) < num_rows:
            categories += ["Unknown"] * (num_rows - len(categories))
        elif len(categories) > num_rows:
            categories = categories[:num_rows]

        df_sorted["Category"] = categories

    except Exception as e:
        st.error(f"An error occurred while calling the API: {e}")
        df_sorted["Category"] = "Error"

    # Show results
    st.write("Values sorted in descending order:")
    st.write(df_sorted)

    # Sum by category
    total = df_sorted["amount"].sum()
    st.write(f"Total: {total:.2f}")

    # Bar chart
    fig = px.bar(
        df_sorted,
        x="title",
        y="amount",
        color="Category",
        title="Bar Chart of Categories",
        labels={"title": "", "amount": "Amount", "Category": "Category"},
    )
    st.plotly_chart(fig, use_container_width=True)

    # Pie chart
    fig = px.pie(
        df_sorted,
        values="amount",
        names="Category",
        title="Pie Chart of Categories",
        labels={"Category": "Category", "amount": "Amount"},
    )

    st.plotly_chart(fig, use_container_width=True)