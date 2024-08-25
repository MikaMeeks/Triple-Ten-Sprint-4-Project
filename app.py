import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('vehicle_us.csv')

# Group by 'model' and sum the 'odometer' values
model_miles = df.groupby('model')['odometer'].sum().reset_index()

# Streamlit app
st.header('Total Miles by Model')

# Plot the data
fig, ax = plt.subplots(figsize=(21, 7))
ax.bar(model_miles['model'], model_miles['odometer'], color='skyblue')
ax.set_xlabel('Model')
ax.set_ylabel('Total Miles')
ax.set_title('Total Miles by Model')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

# Streamlit app
st.title('Miles by Number of Cylinders')

# Create a scatter plot using Plotly Express
fig = px.scatter(df, x='cylinders', y='odometer', 
                 title='Miles by Number of Cylinders',
                 labels={'cylinders': 'Number of Cylinders', 'odometer': 'Miles'},
                 color='cylinders')

# Display the plot in Streamlit
st.plotly_chart(fig)

# Group by 'transmission' and calculate the average 'odometer' values
transmission_avg_miles = df.groupby('transmission')['odometer'].mean().reset_index()

# Streamlit app
st.title('Average Miles by Transmission Type')

# Create a scatter plot using Plotly Express
fig = px.scatter(transmission_avg_miles, x='transmission', y='odometer', 
                 title='Average Miles by Transmission Type',
                 labels={'transmission': 'Transmission Type', 'odometer': 'Average Miles'},
                 color='transmission')

# Display the plot in Streamlit
st.plotly_chart(fig)

# Streamlit app
st.header('Vehicle Listings Analysis')

# Checkbox to show/hide histogram
show_histogram = st.checkbox('Show Price Histogram')

if show_histogram:
    fig_hist = px.histogram(df, x='price', title='Price Distribution')
    st.plotly_chart(fig_hist)

# Scatter plot
fig_scatter = px.scatter(df, x='model_year', y='price', color='condition', title='Price vs. Model Year')
st.plotly_chart(fig_scatter)
