import pandas as pd
import numpy as np

# Generate an array of 10 random numbers
random_numbers = pd.Series(np.random.rand(10))

# Print all numbers
print("All Numbers:")
print(random_numbers)

# Print the first 5 numbers
print("\nFirst 5 Numbers:")
print(random_numbers.head(5))

# Print the last 5 numbers
print("\nLast 5 Numbers:")
print(random_numbers.tail(5))

# Print the first 2 numbers
print("\nFirst 2 Numbers:")
print(random_numbers.head(2))

# Print the last 2 numbers
print("\nLast 2 Numbers:")
print(random_numbers.tail(2))
