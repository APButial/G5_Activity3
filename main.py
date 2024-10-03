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



# Table 6 - Order Status by Product Type - Lim, K.



# Table 7 - Payment Method Distribution - Ongtangco
def pie_chart():
    """
    Payment Methods Distribution in a pie chart format
    """
    df['Payment Method'] = df['Payment Method'].replace({'Paypal': 'PayPal'})

    payment_counts = df['Payment Method'].value_counts()
    labels = payment_counts.index
    pie_colors = ['skyblue', 'salmon', 'yellow', 'lightgreen', 'orange']

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(payment_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=pie_colors)
    ax.set_title('Payment Method Distribution')
    ax.axis('equal')

    # Display the chart
    st.pyplot(fig)

st.header('Payment Method Distribution')
pie_chart()


# Table 8 - Total Sales Overtime - Ongtangco
def line_chart():
    """
    Total sales over time in a line chart format
    """
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    monthly_sales = df.groupby(df['Purchase Date'].dt.to_period('M'))['Total Price'].sum()
    monthly_sales.index = monthly_sales.index.to_timestamp()

    fig, ax = plt.subplots()
    ax.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b', linestyle='-')
    ax.set_title('Total Sales Overtime')
    ax.set_xlabel('Purchase Date (in months)')
    ax.set_ylabel('Total Price (in millions)')
    plt.xticks(rotation=45)

    # Display the chart
    st.pyplot(fig)

st.header('Total Sales Over Time')
line_chart()

# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
