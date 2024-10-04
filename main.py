import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import io

# Note: call [streamlit run main.py] in terminal to test

st.title("Customer Purchase Behavior Analysis Data Visualization")
st.write("""
         **Group Number:** 5\n
         **Section:** BM3\n
         **Group Members:**\n
         * Butial, Aivann Paul
         * Lim, Evan
         * Lim, Kyle Hendrik
         * Ongtangco, Randolph Joshua
         * Tan, Gabriel Christian
         """)

# Read CSV dataset
df = pd.read_csv("dataset/Electronic_sales_Sep2023-Sep2024.csv")
df

# List of cols and dtypes
buffer = io.StringIO()
df.info(buf=buffer)
st.code(buffer.getvalue(), language='text')

# Show missing values
st.dataframe(df.isna().sum())

# Show quantities
st.dataframe(df.describe())

# Table 1 - Gender Distribution - Butial



# Table 2 - Age Distribution - Butial



# Table 3 - Quantity Sold by Product Type - Lim, E.



# Table 4 - Quantity Sold by Smartphone Model - Lim, E.



# Table 5 - Shipping Type by Product Type - Lim, K.
def line_chart():
    df['Shipping Type'] = df['Shipping Type'].replace({'Express': 'Express', 'Standard': 'Standard'})

    monthly_sales = df.groupby('Shipping Type')['Product Type'].count()

    fig, ax = plt.subplots(figsize=(10, 5)) 
    ax.bar(monthly_sales.index, monthly_sales.values, color='b') 
    ax.set_title('Total Sales by Shipping Type')
    ax.set_xlabel('Shipping Type')
    ax.set_ylabel('Total Sales (Count)')
    plt.xticks(rotation=45)

    st.pyplot(fig)

line_chart()

st.write("### Key Observations:")
st.write("- The chart highlights a strong preference for Standard shipping which dwarfs in comparison to other shipping types like Expedited, Express, and Overnight, while Same Day shipping shows the lowest sales count.")

# Table 6 - Order Status by Product Type - Lim, K.
def pie_chart():
    df['Product Type'] = df['Product Type'].replace({
        'smartphone': 'Smartphone',
        'Smartwatch': 'Smartwatch',
        'smartwatch': 'Smartwatch',
        'Tablet': 'Tablet',
        'tablet': 'Tablet',
        'Laptop': 'Laptop',
        'laptop': 'Laptop'
    })

    product_counts = df['Product Type'].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))
    pie_colors = ['skyblue', 'salmon', 'yellow', 'lightgreen', 'orange']
    ax.pie(product_counts, labels=product_counts.index, autopct='%1.1f%%', startangle=140, colors=pie_colors)
    
    ax.set_title('Order Status by Product Type')
    ax.axis('equal')

    st.pyplot(fig)

pie_chart()

st.write("### Key Observations:")
st.write("- This graph highlights that customers prefer smartphones, leading at 29.9%, followed by tablets at 20.5%, laptops and smartwatches at 19.9% and 19.7%, and finally, headphones being the least preferred at 10.1%.")
st.write("- The data showcases a high customer preference for handheld devices such as smartphones and tablets, with their accesssories, like smartwatches and headphones are less prefered.")


# Table 7 - Payment Method Distribution - Ongtangco



# Table 8 - Total Sales Overtime - Ongtangco



# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
