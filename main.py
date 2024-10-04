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
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
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

if __name__ == "__main__":
    st.title("Loyalty Members Over Time Period")
    loyalty_by_time_linechart()
# Conclusion
