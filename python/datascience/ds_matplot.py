import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Create sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['A'], label='Column A', marker='o')
plt.plot(df['B'], label='Column B', marker='s')
plt.plot(df['C'], label='Column C', marker='^')
plt.title('Line Plot of DataFrame Columns')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
# Bar plot
plt.figure(figsize=(10, 6))
df.plot(kind='bar')
plt.title('Bar Plot of DataFrame Columns')
plt.xlabel('Index')
plt.ylabel('Values')
plt.grid(True)
plt.show()
# Histogram
plt.figure(figsize=(10, 6))
df.plot(kind='hist', alpha=0.7, bins=5)
plt.title('Histogram of DataFrame Columns')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['A'], df['B'], c='blue', label='A vs B', marker='o')
plt.scatter(df['A'], df['C'], c='red', label='A vs C', marker='s')
plt.title('Scatter Plot of DataFrame Columns')
plt.xlabel('Column A')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
print("Plots generated successfully.")
# Note: The above code generates plots using matplotlib to visualize the data in the pandas DataFrame.
print("Numpy Array:")
print(data) 