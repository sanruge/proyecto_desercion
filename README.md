Proyecto de Predicción de Deserción Estudiantil 🎓
Este proyecto implementa un sistema de machine learning para predecir si un estudiante universitario se graduará, desertará o continuará inscrito. Incluye un modelo predictivo, una API REST para realizar predicciones y una interfaz visual para usuarios finales.

🔧 Tecnologías utilizadas
Python 3.10+

scikit-learn

FastAPI

Streamlit

Poetry

Pandas, NumPy, Joblib

📁 Estructura del proyecto
csharp
Copiar
Editar
proyecto_desercion/
├── modelo.py
├── modelo_entrenado.joblib
├── api.py
├── app_streamlit.py
├── pyproject.toml
├── poetry.lock
├── README.md
🚀 Cómo ejecutar el proyecto
bash
Copiar
Editar
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
✉️ Contacto
Desarrollado por Santiago Ruge
Maestría en Inteligencia de Negocios
https://www.linkedin.com/in/santiago-ruge