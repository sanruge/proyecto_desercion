import streamlit as st
import requests

st.title("Predicción de Deserción Estudiantil")

st.markdown("Completa la información del estudiante para predecir si se graduará, abandonará o permanecerá inscrito.")

# Formulario
with st.form("formulario_prediccion"):
    col1, col2 = st.columns(2)

    with col1:
        Marital_status = st.number_input("Estado civil (código)", 0, 10)
        Application_mode = st.number_input("Modo de aplicación", 0, 20)
        Application_order = st.number_input("Orden de aplicación", 1, 10)
        Course = st.number_input("Curso (código)", 0, 100)
        Daytime_evening_attendance = st.selectbox("Asistencia", [1, 0])
        Previous_qualification = st.number_input("Educación previa (código)", 0, 20)
        Nacionality = st.number_input("Nacionalidad (código)", 0, 100)
        Mothers_qualification = st.number_input("Escolaridad madre (código)", 0, 20)
        Fathers_qualification = st.number_input("Escolaridad padre (código)", 0, 20)
        Mothers_occupation = st.number_input("Ocupación madre (código)", 0, 20)
        Fathers_occupation = st.number_input("Ocupación padre (código)", 0, 20)
        Displaced = st.selectbox("Desplazado", [0, 1])
        Educational_special_needs = st.selectbox("Necesidades especiales", [0, 1])
        Debtor = st.selectbox("Deudor", [0, 1])
        Tuition_fees_up_to_date = st.selectbox("Pagos al día", [0, 1])
        Gender = st.selectbox("Género", [0, 1])
        Scholarship_holder = st.selectbox("Becado", [0, 1])
        Age_at_enrollment = st.number_input("Edad de ingreso", 15, 70)

    with col2:
        International = st.selectbox("Estudiante internacional", [0, 1])
        Curricular_units_1st_sem_credited = st.number_input("Unidades 1er semestre acreditadas", 0.0, 100.0)
        Curricular_units_1st_sem_enrolled = st.number_input("Unidades 1er semestre inscritas", 0.0, 100.0)
        Curricular_units_1st_sem_evaluations = st.number_input("Evaluaciones 1er semestre", 0.0, 100.0)
        Curricular_units_1st_sem_approved = st.number_input("Unidades aprobadas 1er semestre", 0.0, 100.0)
        Curricular_units_1st_sem_grade = st.number_input("Nota promedio 1er semestre", 0.0, 20.0)
        Curricular_units_1st_sem_without_evaluations = st.number_input("Unidades sin evaluar 1er semestre", 0.0, 10.0)
        Curricular_units_2nd_sem_credited = st.number_input("Unidades 2do semestre acreditadas", 0.0, 100.0)
        Curricular_units_2nd_sem_enrolled = st.number_input("Unidades 2do semestre inscritas", 0.0, 100.0)
        Curricular_units_2nd_sem_evaluations = st.number_input("Evaluaciones 2do semestre", 0.0, 100.0)
        Curricular_units_2nd_sem_approved = st.number_input("Unidades aprobadas 2do semestre", 0.0, 100.0)
        Curricular_units_2nd_sem_grade = st.number_input("Nota promedio 2do semestre", 0.0, 20.0)
        Curricular_units_2nd_sem_without_evaluations = st.number_input("Unidades sin evaluar 2do semestre", 0.0, 10.0)
        Unemployment_rate = st.number_input("Tasa de desempleo", 0.0, 100.0)
        Inflation_rate = st.number_input("Inflación", 0.0, 100.0)
        GDP = st.number_input("PIB", 0.0, 100.0)

    submit = st.form_submit_button("Predecir")

# Enviar a la API
if submit:
    datos = {
        "Marital_status": Marital_status,
        "Application_mode": Application_mode,
        "Application_order": Application_order,
        "Course": Course,
        "Daytime_evening_attendance": Daytime_evening_attendance,
        "Previous_qualification": Previous_qualification,
        "Nacionality": Nacionality,
        "Mothers_qualification": Mothers_qualification,
        "Fathers_qualification": Fathers_qualification,
        "Mothers_occupation": Mothers_occupation,
        "Fathers_occupation": Fathers_occupation,
        "Displaced": Displaced,
        "Educational_special_needs": Educational_special_needs,
        "Debtor": Debtor,
        "Tuition_fees_up_to_date": Tuition_fees_up_to_date,
        "Gender": Gender,
        "Scholarship_holder": Scholarship_holder,
        "Age_at_enrollment": Age_at_enrollment,
        "International": International,
        "Curricular_units_1st_sem_credited": Curricular_units_1st_sem_credited,
        "Curricular_units_1st_sem_enrolled": Curricular_units_1st_sem_enrolled,
        "Curricular_units_1st_sem_evaluations": Curricular_units_1st_sem_evaluations,
        "Curricular_units_1st_sem_approved": Curricular_units_1st_sem_approved,
        "Curricular_units_1st_sem_grade": Curricular_units_1st_sem_grade,
        "Curricular_units_1st_sem_without_evaluations": Curricular_units_1st_sem_without_evaluations,
        "Curricular_units_2nd_sem_credited": Curricular_units_2nd_sem_credited,
        "Curricular_units_2nd_sem_enrolled": Curricular_units_2nd_sem_enrolled,
        "Curricular_units_2nd_sem_evaluations": Curricular_units_2nd_sem_evaluations,
        "Curricular_units_2nd_sem_approved": Curricular_units_2nd_sem_approved,
        "Curricular_units_2nd_sem_grade": Curricular_units_2nd_sem_grade,
        "Curricular_units_2nd_sem_without_evaluations": Curricular_units_2nd_sem_without_evaluations,
        "Unemployment_rate": Unemployment_rate,
        "Inflation_rate": Inflation_rate,
        "GDP": GDP
    }

    # Llamada a la API
    response = requests.post("http://127.0.0.1:8001/predict", json=datos)


    if response.status_code == 200:
        st.success(f"Predicción del modelo: {response.json()['prediccion']}")
    else:
        st.error("Error al obtener la predicción.")
