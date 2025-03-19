import pandas as pd 

dataset_path = 'Titanic-Dataset.csv'
data = pd.read_csv(dataset_path)

print("Primeras 5 filas:")
print(data.head())

print("\nInformacion general de cada columna")
print(data.info())

print("\nDescripcion de la tabla")
print(data.describe())

print("\nValor nulos en columnas")
print(data.isnull().sum())