import pandas as pd

# Cargar los datos desde la ruta completa
ruta = "/Users/santiagoruge/Documents/1. MAESTRIA BI/SEMESTRE 2/SEMINARIO DE PROGRAMACION/PROYECTO/data/data.csv"
df = pd.read_csv(ruta)

# Mostrar las primeras filas del dataset
print(df.head())

print("\nColumnas del dataset:")
print(df.columns)

print("\nResumen de tipos de datos:")
print(df.dtypes)

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nDimensiones del dataset (filas, columnas):", df.shape)

print(df.columns)

# 1. Separar variables predictoras y objetivo
X = df.drop("Target", axis=1)
y = df["Target"]

# 2. Verificamos tipos de columnas
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

print("\nVariables numéricas:")
print(numeric_cols)

print("\nVariables categóricas:")
print(categorical_cols)


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Separar datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Mostrar resultados
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

import joblib

# Guardar el modelo entrenado en un archivo
joblib.dump(modelo, "modelo_entrenado.joblib")
print("\nModelo guardado como 'modelo_entrenado.joblib'")




