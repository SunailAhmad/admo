import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create dummy DataFrame
data = {
    'A': np.random.normal(loc=0, scale=1, size=100),
    'B': np.random.normal(loc=1, scale=2, size=100),
    'C': np.random.normal(loc=-1, scale=0.5, size=100)
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Perform descriptive analysis
print("\nDescriptive statistics of the DataFrame:")
print(df.describe())

# Plot histogram of a column
selected_column = 'A'  # For simplicity, let's choose column 'A'
plt.figure()
sns.histplot(df[selected_column], bins=20, color='skyblue', edgecolor='black')
plt.title(f"Histogram of column '{selected_column}'")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Plot pairplot of selected columns
selected_columns = ['A', 'B']  # For simplicity, let's choose columns 'A' and 'B'
plt.figure()
sns.pairplot(df[selected_columns])
plt.suptitle("Pairplot of selected columns")
plt.show()
