# Proyecto de Predicción de Deserción Estudiantil 🎓

Este proyecto implementa un sistema de machine learning para predecir si un estudiante universitario se graduará, desertará o continuará inscrito. Incluye un modelo predictivo, una API REST para realizar predicciones y una interfaz visual para usuarios finales.

## 🔧 Tecnologías utilizadas

- Python 3.10+
- scikit-learn
- FastAPI
- Streamlit
- Poetry
- Pandas, NumPy, Joblib

## 📁 Estructura del proyecto

proyecto_desercion/ ├── modelo.py ├── modelo_entrenado.joblib ├── api.py ├── app_streamlit.py ├── pyproject.toml ├── poetry.lock ├── README.md

bash
Copiar
Editar

## 🧠 Modelo utilizado y evaluación

Se utilizó un modelo de clasificación **Random Forest** (`RandomForestClassifier` de `scikit-learn`), elegido por su robustez frente a datos con múltiples variables, su capacidad de manejar variables categóricas codificadas y su buen desempeño sin necesidad de un ajuste complejo.

El modelo fue entrenado con un conjunto de datos limpio (sin valores nulos), codificado numéricamente, con un total de 4.424 registros y 34 variables predictoras. La variable objetivo fue `Target`, con tres clases: `"Graduate"`, `"Dropout"` y `"Enrolled"`.

El conjunto de datos se dividió con `train_test_split` en 80% para entrenamiento y 20% para prueba. La evaluación se hizo mediante el reporte de clasificación (`classification_report`), obteniendo los siguientes resultados:

- **Accuracy general**: 0.77
- **Mejor desempeño**: clase `"Graduate"` (f1-score: 0.85)
- **Reto principal**: clase `"Enrolled"` (f1-score: 0.41)

Estos resultados muestran un modelo sólido para tareas de clasificación educativa, con oportunidad de mejora en la clase menos representada.

## 🚀 Cómo ejecutar el proyecto

```bash
git clone https://github.com/sanruge/proyecto_desercion.git
cd proyecto_desercion

# Instalar Poetry si no lo tienes
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"

# Instalar dependencias
poetry install

# Entrenar el modelo
poetry run python modelo.py

# Ejecutar la API
poetry run uvicorn api:app --reload --port 8001

# Ejecutar la interfaz web
poetry run streamlit run app_streamlit.py

```

✉️ Contacto
Desarrollado por Santiago Ruge
Maestría en Inteligencia de Negocios
https://www.linkedin.com/in/santiago-ruge