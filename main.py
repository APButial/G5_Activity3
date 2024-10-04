import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import io

# Note: call [streamlit run main.py] in terminal to test

st.markdown("<h1 style='color: cyan;'>Customer Purchase Behavior Analysis Data Visualization</h1>",
            unsafe_allow_html=True)
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
    st.pyplot(plt)
    plt.clf()

#Call the fucnction
consumer_gender_distribution()

st.write("""
            Customers are almost evenly distributed between male and female, 
            with males leading by only a small difference in percentage.
         """)

# Table 2 - Age Distribution - Butial
#Butial Aivann
def age_distribution():
  """
  customer age distribution in histogram
  """
  size = len(df['Age'])

  # determining number of bins using Sturges' rule
  bins = math.floor(1 + math.log2(size))

  plt.hist(df['Age'].values, bins=bins, color='skyblue', edgecolor='black')
  plt.xlabel('Age')
  plt.ylabel('Frequency')
  plt.title('Customer Age Distribution')
  st.pyplot(plt)
  plt.clf()

age_distribution()

st.write("""
            Many of the customers belong to the age range of **late teens to early twenties**,
            **late forties to early fifties**, and **late seventies**. 
            For the most part, however, customers' ages are **evenly distributed**.
         """)


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
st.write("""
        # Conclusion
        ### Customer Demographics
        * Customers are male and female, and are equally distributed.
        * Customers' ages range from 18 to 80, and are considerably even in distribution as well.

        ### High Demand for Smartphones
        * There is a high demand for smartphone devices.
        * Relevance of online connectivity can be attributed to this demand.

        ### Customer Consistency
        * Based on the observable data 'Loyalty Members' tend to purchase less than 'Non-Members,' exhibiting greater consistency throughout the year, this is according to the analysis of the purchasing behavior.
        * 'Non-Members' show frequent swings in their volume of purchases, which is best seen by a quite notable spike in purchases seen on January 2024.

        ### Increased Electronic Sales in Christmas Season
        * The initial drop in sales at the end of September, followed by a significant surge in December, is most likely due to the holiday shopping spree.
        * Sales began to decrease approaching the end of December. Recovery began in late January, only to be followed up by another sharp decline in the following September.

        ### Best Selling Smartphone Models
        * SKU1004 is leading in sales.
        * Sales of SKU1001 and SMP234 are competitive with SKU1004.

        ### Credits cards and PayPal as Preffered Payment Methods
        * Digital transactions through credit cards and PayPal lead in popularity among payment methods, making up 29.3% and 29.0% respectively.
        * This distribution highlights the clear preference towards digital and convenient payment methods over the traditional methods like cash and debit cards.

        ### Shipping Habits of Customers
        * Customers like standard shipping. It was seen that no matter what the product type, standard shipping has dominated. This suggests that customers want shipping options that are less pricey.
        * For Tablets and Headphones, Same Day and Overnight Shipping were not really that many. So it might suggest that these products are less urgent to the customers, or they want to save up when buying these types of items.

        ### Customer Ratings are Average
        * Customer ratings have been average since they float around the 3 to 3.2 mark.
        * There are big fluctuations around the months of late 2023 to early 2024. The rating since then have been going slightly upward indicating that the company could be making decisions that improve their products or services. The big dip after December 2023, suggest that there are some inconsistencies either with the products or the services the company provides.
        """)