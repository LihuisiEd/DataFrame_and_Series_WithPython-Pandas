import pandas as pd
data = pd.Series([
    {"Name": "John", "Age": 30, "IsStudent": False},
    {"Name": "Alice", "Age": 25, "IsStudent": True},
    {"Name": "Bob", "Age": 35, "IsStudent": False}
])

# Print the Series
print("Complex Data Series:")
for index, item in enumerate(data):
    print(f"Index {index}:")
    for key, value in item.items():
        print(f"    {key}: {value}")

