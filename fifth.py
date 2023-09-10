import pandas as pd

file_path = 'Ventas.csv'
df = pd.read_csv(file_path, delimiter=';')

print(df)

