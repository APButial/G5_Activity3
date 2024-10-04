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
def line_chart():
    df['Shipping Type'] = df['Shipping Type'].replace({'Express': 'Express', 'Standard': 'Standard'})

    monthly_sales = df.groupby('Shipping Type')['Product Type'].count()

    fig, ax = plt.subplots(figsize=(10, 5)) http://localhost:8501/
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
st.write("The majority of customers utilized credit cards (29.3%) and PayPal (29.0%) for payments, followed by bank transfers (19.9%), cash (12.5%), and debit cards (12.4%).")

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
st.write("Sales experienced a decline at the end of September, followed by a significant surge in December. This was followed by a decrease toward the end of December, with a gradual recovery beginning in late January, before sharply declining again at the start of September.")

# Table 9 - Average Rating Over Time - Tan
def average_rating_over_time():
    """
    Creates a line chart showing the average rating over time.
    """
    # Convert 'Purchase Date' to datetime
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    
    # Group by month and calculate average rating
    average_rating = df.groupby(df['Purchase Date'].dt.to_period('M'))['Rating'].mean()

    # Create a line chart 
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')

    # Plot the average rating data
    ax.plot(average_rating.index.astype(str), average_rating.values, color='#83c9ff', linewidth=2, marker='o', label='Average Rating')

    ax.set_title('Average Rating Over Time', color='white')
    ax.set_xlabel('Purchase Month', color='white')
    ax.set_ylabel('Average Rating', color='white')

    ax.tick_params(axis='both', colors='white')

    # Legend
    legend = ax.legend(facecolor='#0e1117', edgecolor='white', fontsize='medium', loc='upper left', framealpha=0.7)
    for text in legend.get_texts():
        text.set_color('white')  

    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Key Observations
    st.write("### Key Observations:")
    st.write("- The average rating showed a steady increase from September 2023 to December 2023..")
    st.write("-  From January 2024 to March 2024, the average rating stabilized, indicating a stable customer perception of the products.")
    st.write("-  Starting from April 2024, there were fluctuations in the observed average rating")
    st.write("- However, a decline in average ratings was observed from June 2024 onwards.")

st.title("Average Rating Over Time Period")
average_rating_over_time()


# Table 10 - Loyalty by Time - Tan
def loyalty_by_time_linechart():
    """
    Creates a line chart showing the number of loyalty members over time.
    """
    # Convert 'Purchase Date' string column to datetime object for easier handling
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

    # Group by month and count the number of unique Loyalty Members
    loyalty_count = df.groupby(df['Purchase Date'].dt.to_period('M'))['Loyalty Member'].apply(lambda x: (x == 'Yes').sum())

    # Create a line chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')

    # Plot the data
    ax.plot(loyalty_count.index.astype(str), loyalty_count.values, marker='o',color='#83c9ff', label='Loyalty Members')

    ax.set_title('Loyalty Members Over Time', color='white')
    ax.set_xlabel('Month', color='white')
    ax.set_ylabel('Number of Loyalty Members', color='white')
    ax.tick_params(axis='both', colors='white')

    # Legend
    legend = ax.legend(facecolor='#0e1117', edgecolor='white', fontsize='medium', loc='upper left', framealpha=0.7)
    for text in legend.get_texts():
        text.set_color('white') 

    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Add Key Observations below the graph
    st.write("### Key Observations:")
    st.write("- The number of loyalty members increased during September 2023 to February 2024, signaling a successful recruitment strategy during this period of time.")
    st.write("- However from March 2024 to May 2024, the number of loyalty members remained relatively stable, meaning the growth rate stabalied during this time.")
    st.write("- And finally the number of loyalty members decreased from June 2024 to September 2024, indicating a potential issue with member retention or a decline in new memberships.")


st.title("Loyalty Members Over Time Period")
loyalty_by_time_linechart()
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