import pandas as pd

# Create a pandas DataFrame with text and numeric values
data = pd.DataFrame({
    "Item": ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape"],
    "Quantity": [10, 5, 8, 12, 6, 9]
})

# Print the original DataFrame
print("Original DataFrame:")
print(data)

# Change the order of the columns
data = data[['Quantity', 'Item']]

# Print the DataFrame with columns reordered
print("\nDataFrame with Columns Reordered:")
print(data)
