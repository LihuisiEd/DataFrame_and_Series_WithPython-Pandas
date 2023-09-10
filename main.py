import pandas as pd
# Create a pandas Series with more items
fruits = pd.Series(["banana", "apple", "peach", "orange", "grape", "strawberry"])

# Reorder the items in the Series
reordered_fruits = pd.concat([fruits[2:], fruits[:2]], ignore_index=True)

# Print original array
print("Fruits Series:")
for index, item in enumerate(fruits):
    print(f"Index {index}: {item}")

# Print the reordered Series
print("Reordered Fruits Series:")
for index, item in enumerate(reordered_fruits):
    print(f"Index {index}: {item}")

