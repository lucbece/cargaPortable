import os
import pandas as pd

path = 'C:/Users/Lucas/Desktop/Carga_de_Muestras_V2/database'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xlsx' in file:
            files.append(os.path.join(r, file))

for f in files:

    df = pd.read_excel(files[f])
    Equipos = df['Equipo']
    Componente = df['Componente']
    Punto_Extraccion = df['P.E']
    Fecha = df['Fecha']

    Muestras = []

    for i in range(len(Equipos)):
        for j in range(len(Equipos)):
            if Equipos[i] == Equipos[j] and i =! j:
                if Componente[i] == Componente[j]:
                    if Punto_Extraccion[i] == Punto_Extraccion[j]:
                        
    
    