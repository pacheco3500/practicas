import pandas as pd

datase_path = 'Titanic-Dataset.csv'
data = pd.read_csv(datase_path)

print("Primeras 5 filas:")
print(data.head())

print("\nUltimas 5 filas")
print(data.tail())

print("\nInformacion general de la columna")
print(data.info())

print("\nDescripcion de la tabla")
print(data.describe())

print("\nValores nulos en columna")
print(data.isnull().sum())