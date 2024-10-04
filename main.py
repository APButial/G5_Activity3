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
def quantity_sold_by_prodtype():
  """
  quantity sold by product type in bar chart
  """
  # only completed orders will be considered sold via boolean masking
  completed_orders = df['Order Status'] == 'Completed'
  filtered = df.where(completed_orders).dropna()

  # creates an array of quantity sold indexed by product type
  quantity_sold_array = filtered['Quantity'].groupby(filtered['Product Type']).sum().sort_values()

  colors = ['skyblue', 'orange', 'salmon', 'lightgreen', 'yellow']
  plt.bar(quantity_sold_array.index, quantity_sold_array.values, color=colors, edgecolor='black')
  plt.xlabel('Product Type')
  plt.ylabel('Quantity Sold')
  plt.title('Quantity Sold by Product Type')
  plt.show()


quantity_sold_by_prodtype()

#Observation
#Smartphone devices have the highest quantity sold among other electronics. Over **16,000** were sold from September 2023 to September 2024. On the other hand, **headphones** have the least quantity sold of less than **60,000**. Smartwatches, laptops, and tablets, sold were relatively equal.




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

#Observation
#The smartphone model SKU1004 has the highest numbers sold, while the SKU1005 being the least bought. Still, the numbers sold by SKU1001 and SMP234 are comparable to SKU1004. These three models are selling well.


# Table 5 - Shipping Type by Product Type - Lim, K.



# Table 6 - Order Status by Product Type - Lim, K.



# Table 7 - Payment Method Distribution - Ongtangco



# Table 8 - Total Sales Overtime - Ongtangco



# Table 9 - Average Rating Over Time - Tan



# Table 10 - Loyalty by Time - Tan



# Conclusion
