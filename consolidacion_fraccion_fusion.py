#python36
import pandas as pd
import glob
import tkinter.filedialog, re
import time
import os
import os.path

starttime =  time.time()

#para solicitar la carpeta donde estan los archivos
root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askdirectory()

#listado con nombres de archivos csv de la carpeta
print("Leyendo los archivos")
interesting_files=[]
os.chdir(file_path)
for file in glob.glob("*.csv"):
    interesting_files.append(file)

print("Eliminando los archivos sin datos")
for i in interesting_files:
    if (pd.read_csv(i,encoding='latin1', usecols=[0,1,2,3,4,5,6,7])).size==0:
        os.remove(i)

print('Borrando consolidado anterior')
if "output.csv" in interesting_files:
    os.remove("output.csv")

#nuevo listado con nombre de los archivos csv que quedaron
nombre_archivos=[]
os.chdir(file_path)
for file in glob.glob("*.csv"):
    nombre_archivos.append(file)

#para poder leer los archivos con las columnas necesarias y guardarlos en otra lista como dataframe con las modificaciones necesarias
archivos_modificados=[]
for i in nombre_archivos:
    archivos_modificados.append(pd.read_csv(i,encoding='latin1', usecols=[0,1,2,3,4,5,6,7]))

#lista de codigos
print("Extrayendo los codigos de los nombres")
codigos=[]
for i in nombre_archivos:
	codigos.append(str(i[0:3]))

print("Escribiendo los codigos dentro de los archivos")
for j in range(0,len(archivos_modificados)):
	archivos_modificados[j].loc[0,"SERVICIO"]=""
	for i in range(0, len(archivos_modificados[j])):
		archivos_modificados[j].loc[i,"SERVICIO"]=codigos[j]

print("Guardando los archivos modificados")
for i in range(0,len(archivos_modificados)):
	archivos_modificados[i].to_csv(str("archivo"+str(i)+".csv"),encoding='latin1', index=False)

print("Consolidando")
df_list = []
for i in range(0,len(archivos_modificados)):
	df_list.append(archivos_modificados[i])

full_df = pd.concat(df_list)

full_df.to_csv('output.csv', index=False)

print ("Archivo guardado")

input()
