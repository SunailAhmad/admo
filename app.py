import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Create dummy DataFrame
data = {
    'A': np.random.normal(loc=0, scale=1, size=100),
    'B': np.random.normal(loc=1, scale=2, size=100),
    'C': np.random.normal(loc=-1, scale=0.5, size=100)
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
st.write("First few rows of the DataFrame:")
st.write(df.head())

# Perform descriptive analysis
st.write("\nDescriptive statistics of the DataFrame:")
st.write(df.describe())

# Plot histogram of a column
selected_column_hist = st.selectbox("Select a column for histogram", df.columns)
plt.figure()
sns.histplot(df[selected_column_hist], bins=20, color='skyblue', edgecolor='black')
plt.title(f"Histogram of column '{selected_column_hist}'")
plt.xlabel("Value")
plt.ylabel("Frequency")
st.pyplot()

# Plot pairplot of selected columns
selected_columns_pairplot = st.multiselect("Select columns for pairplot", df.columns)
plt.figure()
sns.pairplot(df[selected_columns_pairplot])
plt.suptitle("Pairplot of selected columns")
st.pyplot()
