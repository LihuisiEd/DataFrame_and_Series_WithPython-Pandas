import pandas as pd

# Read the CSV file into a pandas DataFrame
ventas_data = pd.read_csv('Ventas.csv', delimiter=';')

# Extract the sales data for the first quarter (January, February, and March)
first_quarter_sales = ventas_data.loc[ventas_data['Meses'].isin(['Enero', 'Febrero', 'Marzo'])]

# Print the sales data for the first quarter
print("Sales Data for the First Quarter:")
print(first_quarter_sales)

# Extract the sales amounts as a numeric array
sales_amounts = first_quarter_sales['Monto'].astype(float)

# Calculate and print the statistics
print("\nStatistics for First Quarter Sales:")
print(f"Mean: {sales_amounts.mean()}")
print(f"Correlation:\n{sales_amounts.corr()}")
print(f"Minimum Value: {sales_amounts.min()}")
print(f"Maximum Value: {sales_amounts.max()}")
print(f"Median: {sales_amounts.median()}")
print(f"Standard Deviation: {sales_amounts.std()}")
