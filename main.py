import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import io

# Note: call [streamlit run main.py] in terminal to test
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

# functions #############################################################################
#Lim, E
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
    st.write("""
            Customers are almost evenly distributed between male and female, 
            with males leading by only a small difference in percentage.
         """)
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
  st.write("""
            Many of the customers belong to the age range of **late teens to early twenties**,
            **late forties to early fifties**, and **late seventies**. 
            For the most part, however, customers' ages are **evenly distributed**.
         """)
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
  st.pyplot(plt)
  plt.clf()
  st.write("""
            **Smartphone devices** have the highest quantity sold among other electronics. 
           Over **16,000** were sold from September 2023 to September 2024. On the other hand, 
           **headphones** have the least quantity sold of less than **60,000**. Smartwatches, laptops, 
           and tablets, sold were relatively equal.
           """)
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
    st.pyplot(plt)
    plt.clf()
    st.write("""
             The smartphone model **SKU1004** has the highest numbers sold, 
             while the **SKU1005** being the least bought. Still, 
             the numbers sold by **SKU1001** and **SMP234** are comparable to SKU1004. 
             These three models are selling well.
         """)
#Ongtangco, Randolph Joshua
def shipping_type_by_product_bar():
    """
        bar chart
        shows shipping type distribution by product type
    """
    # Product Type and Shipping Type grouped seperately
    shipping_by_product = df.groupby(['Product Type', 'Shipping Type']).size().unstack(fill_value=0)
    shipping_by_product.plot(kind='bar', stacked=True, color=['lightblue', 'salmon', 'green', 'red', 'orange'])

    # Title + labels
    plt.title('Shipping Type by Product Type')
    plt.xlabel('Product Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Shipping Type')
    st.pyplot(plt)
    plt.clf()
    st.write("""
              The bar chart represents the shipping preference for different types of products: Headphones, Laptops, Smartphones, Smartwatches, and Tablets. 
              As the chart is a stacked bar chart, each bar will show the proportion of use of shipping methods for any given category of product. 
              This will easily compare the shipping preferences across the various products-understand customer behaviors and tendencies when purchasing these electronics.
              \n\n
              Observations:
              *   Standard Shipping (orange) leads in most product categories, highly dominant in Smartphones.
              *   Same Day Shipping (red) proves to be more popular for Laptops and Smartphones. This means that customers want their products delivered sooner, indicating, maybe, they want to receive their devices as quickly as they can.
              *   Most categories have an almost equal balance of Overnight Shipping (green) and Express Shipping (pink), though both these modes are taken up less than Standard and Same Day.
             """)
#Tan Gabriel
def order_status_by_prod_type():
    """
    bar chart showing the frequency of order status
    (Completed vs Canceled) by product type.
    """
    # filters if status order is either completed or cancelled via boolean masking
    orderstat = df['Order Status'].isin(['Completed', 'Cancelled'])
    # creas a df containing only the relevant orders
    filter = df[orderstat]
    #creates a df to count the number of orders by Product Type and Order Status
    order_fre = filter.groupby(['Product Type', 'Order Status']).size().unstack(fill_value=0)
    # colors :D
    colors = ['red', 'skyblue']
    # creating a bar chart from the new df order_fre
    order_fre.plot(kind='bar', color=colors, edgecolor='black', figsize=(10, 6))
    plt.xlabel('Product Type')
    plt.ylabel('Frequency')
    plt.title('Order Status by Product Type')
    plt.xticks(rotation=30)
    plt.legend(title='Order Status')
    
    st.pyplot(plt)
    plt.clf()
    st.write("""
             For all products, the number of 'Completed' purchases significantly outweighs 
             the number of cancelled purchases, indicating a strong satifaction/interest with 
             the various products offered. Most pruchased product being 'SmartPhones' seconded 
             by 'Tablet'. Meanwhile the most 'Cancelled' is 'Smartphones' seconded by 'Tablet' once again.
             """)

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
  st.header('Payment Method Distribution')
  st.pyplot(fig)
  st.write("""
            The majority of customers utilized credit cards (29.3%) and PayPal (29.0%) for payments, 
            followed by bank transfers (19.9%), cash (12.5%), and debit cards (12.4%).
            """)
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
    st.write("""
             Sales experienced a decline at the end of September, 
             followed by a significant surge in December. This was followed 
             by a decrease toward the end of December, with a gradual recovery 
             beginning in late January, before sharply declining again at the 
             start of September.
             """)
  #Ongtangco, Randolph Joshua
def average_rating_over_time_linechart():
    """
        line chart
        shows the average rating of products over time
    """

    # 'Purchase Date' column -> datetime object
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

    # Purchase Date >> grouped
    # Mean rating per day >> calculated
    average_rating_by_month = df.groupby(df['Purchase Date'].dt.to_period('M'))['Rating'].mean()
    plt.figure(figsize=(25, 4))
    plt.plot(average_rating_by_month.index.astype(str), average_rating_by_month, marker='.', color='red')

    # Title + labels
    plt.title('Monthly Average Rating')
    plt.xlabel('Purchase Date')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
    st.write("""
              The following graph represents the average rating given by the customers from September 2023 to September 2024. 
              This graph is intended to demonstrate the trend of customer satisfaction on a 
              monthly basis. It could possibly be useful in determining periods when customer satisfaction improved or worsened 
              and might point to possible quality problems or improvement initiated by the company.
              \n\n
              **Observations:**

              * There is a spiking in ratings in October 2023. Rating dips slightly in November 2023 but peaks during December 2023.
              * Ratings then drop sharply in January 2024-one of the lowest ratings. Could be post-holiday decline or service/product issue during those times.
              * There is a slight recovery of the ratings during February 2024 to September 2024, but has never reach the heights as rating during late 2023.
            """)
    #Tan Gabriel
def loyalty_by_time_linechart():
    """
    creates a line char showing the number of purchases made by
    loyalty members vs non-members over  a period of time.
    """
    # converts 'Purchase Date' string collumn to datetime object for easier
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

    # groupby Purchase Date and  Member status, then count frequency
    p_by_loyalty = df.groupby([df['Purchase Date'].dt.date, 'Loyalty Member']).size().unstack(fill_value=0)
    plt.figure(figsize=(20, 6))
    plt.plot(p_by_loyalty.index, p_by_loyalty['Yes'], marker='', label='Loyalty Member', color='blue')
    plt.plot(p_by_loyalty.index, p_by_loyalty['No'], marker='', label='Non-Member', color='red')
    plt.title('Purchases by Loyalty Members Over Time Period')
    plt.xlabel('Date of Purchase')
    plt.ylabel('Number of Purchases')
    plt.xticks(rotation=30)
    plt.legend(title='Loyalty Member')
    plt.grid()
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()
    st.write("""
            'Loyalty Member's tend to purchase less than 'Non-Member's with more 
             consistency throuhout the year.Whereas 'Non-Member's tend to purchase 
             more and with more  fluctuation through the year shown in the sharp increase at 
             2024-01.
             """)
def conclusion():
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
############################################################################################
# Graph 1 - Gender Distribution - Butial
consumer_gender_distribution()
# Graph 2 - Age Distribution - Butial
age_distribution()
# Graph 3 - Quantity Sold by Product Type - Lim, E.
quantity_sold_by_prodtype()
# Graph 4 - Quantity Sold by Smartphone Model - Lim, E.
quantity_sold_by_smartphone_model()
# Graph 5 - Shipping Type by Product Type - Lim, K.    
shipping_type_by_product_bar()
# Graph 6 - Order Status by Product Type - Lim, K.
order_status_by_prod_type()
# Graph 7 - Payment Method Distribution - Ongtangco
pie_chart()
# Graph 8 - Total Sales Overtime - Ongtangco
line_chart()
# Graph 9 - Average Rating Over Time - Tan
average_rating_over_time_linechart()
# Graph 10 - Loyalty by Time - Tan
loyalty_by_time_linechart()
# Conclusion
conclusion()