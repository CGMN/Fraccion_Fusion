

import pandas as pd
import glob
interesting_files = glob.glob("*.csv")

#para poder leer los archivos con las columnas necesarias y guardarlos en otra lista con las modificaciones necesarias
archivos_modificados=[]
for i in interesting_files:
	archivos_modificados.append(pd.read_csv(i,encoding='latin1', usecols=[0,1,2,3,4,5,6,7]))


#lista de codigos
codigos=[]
for i in range(0,len(interesting_files)):
	codigos.append(str(interesting_files[i][0:4]))

#Para escribir los codigos dentro del archivo
for j in range(0,len(archivos_modificados)):
	archivos_modificados[j].loc[0,"SERVICIO"]=""
	for i in range(0, len(archivos_modificados[j])):
		archivos_modificados[j].loc[i,"SERVICIO"]=codigos[j]

#para guardar los archivos modificados
for i in range(0,len(interesting_files)):
	archivos_modificados[i].to_csv(str(interesting_files[i]),encoding='utf-8', index=False)


df_list = []
for filename in interesting_files:
    df_list.append(pd.read_csv(filename))

full_df = pd.concat(df_list)

full_df.to_csv('output.csv', index=False)
