import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# SE CARGA BASE DE DATOS

db = pd.read_csv(r'C:\Users\PC\PythonProjects\tensorEnv\db.csv')


# Se define la variable X como AÑO - 2019 + MES / 12

def data_convert(año, mes):
    return (año - 2019) + mes / 12


db['X_axis'] = data_convert(db['Año'], db['Mes'])

# Se definen las variables dependiente (X) e independiente (Y) del modelo

y = db['Interacciones'].to_numpy()
x = db['X_axis'].to_numpy().reshape((-1, 1))

# Se genera el modelo de regresión lineal

model = LinearRegression().fit(x, y)

# Se imprime el resultado de la regresión

print('BETA0: %s' % model.intercept_)
print('BETA1 %s' % model.coef_[0])
print('R: %s' % model.score(x, y))

# Se genera la predición de los valores y se grafican
y_model = model.predict(x)
plt.plot(x, y, 'yo', x, y_model, '--k')
plt.show()

# Predicción de los 3 datos siguientes

año_pred = np.array([2021, 2021, 2021])
mes_pred = np.array([1, 2, 3])

x_pred = data_convert(año_pred, mes_pred).reshape((-1, 1))
y_pred = model.predict(x_pred)

# Grafica de los datos predecidos.

plt.bar(mes_pred, y_pred)
plt.show()
