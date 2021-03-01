# Ejercicio 1
#importa pandas
import pandas as pd
pandas.__version__
# Crea una Serie de los numeros 10, 20 and 10.

numeros=pd.Series([10,20,10])

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
objetos=pd.Series(["rojo", "verde", "azul"])
# Crea un dataframe vacío llamado 'df'
df=pd.DataFrame
df

# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
dic={}
dic["numero"]=numeros
df=pd.DataFrame(dic)
df
# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
dic["objeto"]=objetos
df=pd.DataFrame(dic)
df
# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
avengers = pd.read_csv('./data/pandas/avengers.csv')
avengers
# Muestra las primeras 5 filas del DataFrame.
avengers.head()
# Muestra las primeras 10 filas del DataFrame. 
avengers.head(10)
# Muestra las últimas 5 filas del DataFrame.

avengers.tail()
# Muestra el tamaño del DataFrame
avengers.shape
# Muestra los data types del dataframe
avengers.dtypes 
# Cambia el indice a la columna "fecha_inicio".

df2 = df.set_index("fecha_inicio")
df2
# Ordena el índice de forma descendiente
df_sorted = avengers.sort_values(by="fecha_inicio", ascending=False)
df_sorted.head()
# Ejercicio 2
import pandas as pd
airbnb = pd.read_csv("./data/pandas/airbnb.csv")

airbnb.head()
#ugares con más de 10 críticas con una puntuación mayor de 4
#debemos mostrar antes aquellas con más críticas.
df=airbnb[(airbnb["reviews"]>10) & (airbnb["overall_satisfaction"]>4)]
df_sorted = df.sort_values(by="reviews", ascending=False)
df_sorted.head(3)
# Ejercicio 3
# Ejercicio 4
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
    n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])