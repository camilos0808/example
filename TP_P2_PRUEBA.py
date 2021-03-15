import pandas as pd
import matplotlib.pyplot as plt

# Se lee el archivo de Excel
db = pd.read_excel(r'C:\Users\PC\PythonProjects\tensorEnv\BD_Prueba_tecnica.xlsx', engine='openpyxl')

#  Se eliminan los valores nulos
db = db.loc[(~db['Score A'].isnull()) | (~db['Score B'].isnull())].copy().copy()

# Se crea filtra BD y se calculan las estadisticas de los Score
db = db[['Estado Cliente al final del periodo','Churn Total', 'Score B', 'Score A']]
descr_AB = db.describe()[['Score A', 'Score B']]

# Se calcula el promedio de las Scores agruapdos por Estado
mean_state = db.groupby(by='Estado Cliente al final del periodo').mean()

# Se grafica histograma de los Scores

columna = 'Score B'
hist = db[columna].hist(by=db['Estado Cliente al final del periodo'], bins=20)

plt.show()

columna = 'Score A'
hist = db[columna].hist(by=db['Estado Cliente al final del periodo'], bins=20)

plt.show()