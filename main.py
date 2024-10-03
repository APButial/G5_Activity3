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



# Table 8 - Total Sales Overtime - Ongtangco



# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
