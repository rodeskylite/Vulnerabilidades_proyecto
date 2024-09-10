import pandas as pd
import os

# Lista de archivos .xlsx
file_paths = [
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Container Vuln for the Acc-458043125340 (1).xlsx',
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Container Vuln for the Acc-977263292974 (1).xlsx',
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Container Vulnerability_160552070070.xlsx',
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Container Vulnerability_670557586222 (1).xlsx',
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Container Vulnerability_966582997400 (1).xlsx',
    'C:/Users/rodag/OneDrive/Documentos/Magister/PROYECTO INTEGRADO/Vulnerabilidades/Vulnerabilidades 04-09-24/AWS Contianer Vuln for the Acc-110591430312 (1).xlsx'
]

# DataFrames vacíos para almacenar las hojas
registry_combined = pd.DataFrame()
serverless_combined = pd.DataFrame()

# Iterar sobre los archivos
for file_path in file_paths:
    # Cargar el archivo Excel
    xls = pd.ExcelFile(file_path)
    
    # Leer la pestaña 'Registry 04_09_24' si existe
    if 'Registry 04_09_24' in xls.sheet_names:
        registry_df = pd.read_excel(xls, 'Registry 04_09_24')
        registry_combined = pd.concat([registry_combined, registry_df], ignore_index=True)
    
    # Leer la pestaña 'Serverless 04_09_24' si existe
    if 'Serverless 04_09_24' in xls.sheet_names:
        serverless_df = pd.read_excel(xls, 'Serverless 04_09_24')
        serverless_combined = pd.concat([serverless_combined, serverless_df], ignore_index=True)

# Guardar los DataFrames combinados en un nuevo archivo .xlsx
with pd.ExcelWriter('Vulnerabilidades_Misiones.xlsx') as writer:
    registry_combined.to_excel(writer, sheet_name='Registry 04_09_24', index=False)
    serverless_combined.to_excel(writer, sheet_name='Serverless 04_09_24', index=False)

print("Archivo 'Vulnerabilidades_Misiones.xlsx' generado correctamente.")
