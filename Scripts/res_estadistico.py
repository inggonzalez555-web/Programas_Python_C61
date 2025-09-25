# importa las librerías necesarias
import numpy as np 
import pandas as pd 
import argparse

#Creae un objeto de coneccion
parser = argparse.ArgumentParser(description= "Resumen estadistico")
parser.add_argument("input",help="archivo csv")

args = parser.parse_args() 
df= pd.read_csv(args.input)

print(df.describe())


#Dentro de la carpeta Scripts cree un programa llamado res_estadistico.py que reciba como input desde la consola un archivo csv con un solo conjunto de datos, y retorne como resultado un resumen estadístico que incluya los siguientes indicadores:
#Tamaño de la muestra
#Media
#Mediana
#Cuartil 1
#Cuartil 2
#Rango Interquartil
#Para probar que su script funciona puede probar con el siguiente conjunto de datos: