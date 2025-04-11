from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar el modelo entrenado
modelo = joblib.load("modelo_entrenado.joblib")

# Crear la aplicación
app = FastAPI()

# Definir la estructura de datos esperada
class Estudiante(BaseModel):
    Marital_status: int
    Application_mode: int
    Application_order: int
    Course: int
    Daytime_evening_attendance: int
    Previous_qualification: int
    Nacionality: int
    Mothers_qualification: int
    Fathers_qualification: int
    Mothers_occupation: int
    Fathers_occupation: int
    Displaced: int
    Educational_special_needs: int
    Debtor: int
    Tuition_fees_up_to_date: int
    Gender: int
    Scholarship_holder: int
    Age_at_enrollment: int
    International: int
    Curricular_units_1st_sem_credited: float
    Curricular_units_1st_sem_enrolled: float
    Curricular_units_1st_sem_evaluations: float
    Curricular_units_1st_sem_approved: float
    Curricular_units_1st_sem_grade: float
    Curricular_units_1st_sem_without_evaluations: float
    Curricular_units_2nd_sem_credited: float
    Curricular_units_2nd_sem_enrolled: float
    Curricular_units_2nd_sem_evaluations: float
    Curricular_units_2nd_sem_approved: float
    Curricular_units_2nd_sem_grade: float
    Curricular_units_2nd_sem_without_evaluations: float
    Unemployment_rate: float
    Inflation_rate: float
    GDP: float

@app.post("/predict")
def predecir(estudiante: Estudiante):
    datos = pd.DataFrame([estudiante.dict()])

    # Renombrar columnas al formato usado en el entrenamiento del modelo
    columnas_originales = {
        "Marital_status": "Marital status",
        "Application_mode": "Application mode",
        "Application_order": "Application order",
        "Course": "Course",
        "Daytime_evening_attendance": "Daytime/evening attendance",
        "Previous_qualification": "Previous qualification",
        "Nacionality": "Nacionality",
        "Mothers_qualification": "Mother's qualification",
        "Fathers_qualification": "Father's qualification",
        "Mothers_occupation": "Mother's occupation",
        "Fathers_occupation": "Father's occupation",
        "Displaced": "Displaced",
        "Educational_special_needs": "Educational special needs",
        "Debtor": "Debtor",
        "Tuition_fees_up_to_date": "Tuition fees up to date",
        "Gender": "Gender",
        "Scholarship_holder": "Scholarship holder",
        "Age_at_enrollment": "Age at enrollment",
        "International": "International",
        "Curricular_units_1st_sem_credited": "Curricular units 1st sem (credited)",
        "Curricular_units_1st_sem_enrolled": "Curricular units 1st sem (enrolled)",
        "Curricular_units_1st_sem_evaluations": "Curricular units 1st sem (evaluations)",
        "Curricular_units_1st_sem_approved": "Curricular units 1st sem (approved)",
        "Curricular_units_1st_sem_grade": "Curricular units 1st sem (grade)",
        "Curricular_units_1st_sem_without_evaluations": "Curricular units 1st sem (without evaluations)",
        "Curricular_units_2nd_sem_credited": "Curricular units 2nd sem (credited)",
        "Curricular_units_2nd_sem_enrolled": "Curricular units 2nd sem (enrolled)",
        "Curricular_units_2nd_sem_evaluations": "Curricular units 2nd sem (evaluations)",
        "Curricular_units_2nd_sem_approved": "Curricular units 2nd sem (approved)",
        "Curricular_units_2nd_sem_grade": "Curricular units 2nd sem (grade)",
        "Curricular_units_2nd_sem_without_evaluations": "Curricular units 2nd sem (without evaluations)",
        "Unemployment_rate": "Unemployment rate",
        "Inflation_rate": "Inflation rate",
        "GDP": "GDP"
    }

    datos.rename(columns=columnas_originales, inplace=True)

    # Realizar predicción
    prediccion = modelo.predict(datos)[0]
    return {"prediccion": prediccion}
