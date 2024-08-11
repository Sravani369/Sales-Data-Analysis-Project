import matplotlib.pyplot as plt
import seaborn as sns

# Display the first few rows of the data
print(df.head())

# Analyze trends and patterns
sales_trends = df.groupby('Date')['Sales'].sum().reset_index()

# Create a line plot for sales trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Sales', data=sales_trends)
plt.xticks(rotation=45)
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
