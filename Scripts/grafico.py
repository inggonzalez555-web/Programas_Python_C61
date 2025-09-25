# importa las librerías necesarias
import numpy as np 
import pandas as pd 
import argparse

#Creae un objeto de coneccion
parser = argparse.ArgumentParser(description= "programa que genera un histograma por los datos dados")
parser.add_argument("media",help="valor promedio del histograma")
parser.add_argument("desv",help="Error estándar del histograma")
parser.add_argument("--n",default=100,help="Tamaño de la muestra a graficar") #Opcional

args = parser.parse_args() 

n = int(args.n)
media = float(args.media)
desv = float(args.desv)

#Genera datos aleatorios con distribución normal
datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

#Elimina datos atípicos (outliers)
datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 
#crea un DataFrame de pandas para agrupar los datos

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 
histograma = datos_trim.groupby('Datos').size() 
#imprime el histograma

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )