import pandas as pd

# Create the first DataFrame with city names and population
cities1 = pd.DataFrame({
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Population": [8537673, 39776830, 2705994, 2303482, 1680992, 1584064]
})

# Create the second DataFrame with additional city data
cities2 = pd.DataFrame({
    "City": ["San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville"],
    "Population": [1547253, 1419480, 1345047, 1035317, 1033674, 903889]
})

# Print the first DataFrame
print("First DataFrame:")
print(cities1)

# Print the second DataFrame
print("\nSecond DataFrame:")
print(cities2)

# Add the values of the second DataFrame to the first one
resulting_cities = cities1.add(cities2, fill_value=0)

# Print the resulting DataFrame
print("\nResulting DataFrame after Addition:")
print(resulting_cities)
