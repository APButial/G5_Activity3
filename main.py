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

  #CSV file has multiple instances of PayPal being spelled with a lower case p (Paypal)
  #Following code allows for PayPal and Paypal to be treated as the same value
  df['Payment Method'] = df['Payment Method'].replace({'PayPal': 'PayPal', 'Paypal': 'PayPal'})


  payment_counts = df['Payment Method'].value_counts()
  labels = payment_counts.index
  pie_colors = ['skyblue', 'salmon', 'yellow', 'lightgreen', 'orange']
  plt.figure(figsize=(8, 8))
  plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, colors=pie_colors, )
  plt.title('Payment Method Distribution')
  plt.axis('equal')
  plt.show()

pie_chart()


# Table 8 - Total Sales Overtime - Ongtangco
def line_chart():
  """
  Total sales over time in a line chart format
  """

  df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
  monthly_sales = df.groupby(df['Purchase Date'].dt.to_period('M'))['Total Price'].sum()
  monthly_sales.index = monthly_sales.index.to_timestamp()

  plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b', linestyle='-')

  plt.title('Total Sales Overtime')
  plt.xlabel('Purchase Date (in months)')
  plt.ylabel('Total Price (in millions)')
  plt.xticks(rotation=45)
  plt.show()

line_chart()

# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
