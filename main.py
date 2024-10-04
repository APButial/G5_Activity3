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

# Table 1 - Gender Distribution - Lim, E.
#Lim Evan
def consumer_gender_distribution():
    """
    Displays a pie chart showing the gender distribution of consumers
    """

    # Counts the number of each gender
    gender_counts = df['Gender'].value_counts()

    # Sets the Label in the Pie Chart
    labels = gender_counts.index

    # Sets the color in each gender
    colors = ['skyblue', 'pink']

    #Creating and Setting up the Pie Chart
    plt.figure(figsize=(8,8))
    plt.pie(gender_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Consumer Gender Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

#Call the fucnction
consumer_gender_distribution()


# Table 2 - Age Distribution - Butial



# Table 3 - Quantity Sold by Product Type - Butial



# Table 4 - Quantity Sold by Smartphone Model - Lim, E.
#Lim Evan
def quantity_sold_by_smartphone_model():
    """
    Displays a bar chart showing the quantity sold by smartphone model (SKU).
    Only completed orders are considered sold.
    """
    # Completed Orders will only be the one considered
    completed_orders = df['Order Status'] == 'Completed'
    filtered = df.where(completed_orders).dropna()

    # Filters to only Devices that are smartphone
    smartphone_data = filtered[filtered['Product Type'] == 'Smartphone']

    # sum of sold smartphone models per model
    quantity_sold_array = smartphone_data.groupby('SKU')['Quantity'].sum().sort_values()

    # Array containing Color of bars in the chart
    colors = ['pink', 'red', 'green', 'blue']

    #Creates the bar chart
    plt.bar(quantity_sold_array.index, quantity_sold_array.values, color=colors, edgecolor='black')
    plt.title('Numbers of Sold Smartphone Models')
    plt.xlabel('Smartphone Models')
    plt.ylabel('Number Sold')
    plt.tight_layout()
    plt.show()

#Calls the function quantity_sold_by_smartphone_model()
quantity_sold_by_smartphone_model()


# Table 5 - Shipping Type by Product Type - Lim, K.



# Table 6 - Order Status by Product Type - Lim, K.



# Table 7 - Payment Method Distribution - Ongtangco



# Table 8 - Total Sales Overtime - Ongtangco



# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
