import pandas as pd

# Cargar el archivo Excel
file_path = 'Vulnerabilidades_Misiones.xlsx'
xls = pd.ExcelFile(file_path)

# Cargar las hojas necesarias
registry_df = pd.read_excel(xls, 'Registry 04_09_24')
serverless_df = pd.read_excel(xls, 'Serverless 04_09_24')

# Mostrar las primeras filas de cada hoja para verificar
print(registry_df.head())
print(serverless_df.head())
