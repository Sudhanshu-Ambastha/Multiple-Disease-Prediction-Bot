# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:22:52 2023

@author: sudha
"""

import streamlit as st
import pickle

# Define a custom CSS class for emoji icons
custom_css = """
<style>
    .emoji-icon {
        font-size: 24px;
        vertical-align: middle;
        padding-right: 12px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Disease dictionary with symptoms
disease_data = {
    "Fungal infection": ["itching", "skin_rash", "nodal_skin_eruptions"],
    "Hepatitis C": ["continuous_sneezing", "shivering", "chills"],
    "Hepatitis E": ["joint_pain", "stomach_pain", "acidity"],
    "Alcoholic hepatitis": ["ulcers_on_tongue", "muscle_wasting", "vomiting"],
    "Tuberculosis": ["cough", "high_fever", "sweating"],
    "Common Cold": ["continuous_sneezing", "chills", "fatigue"],
    "Pneumonia": ["high_fever", "sweating", "breathlessness"],
    "Dimorphic hemmorhoids(piles)": ["bleeding", "pain_during_bowel_movements", "bloody_stool"],
    "Heart attack": ["chest_pain", "weakness_in_limbs", "fast_heart_rate"],
    "Varicose veins": ["swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes"],
    "Hypothyroidism": ["fatigue", "weight_gain", "cold_hands_and_feets"],
    "Hyperthyroidism": ["mood_swings", "weight_loss", "restlessness"],
    "Hypoglycemia": ["lethargy", "patches_in_throat", "irregular_sugar_level"],
    "Osteoarthristis": ["pain_in_joints", "muscle_weakness", "stiff_neck"],
    "Arthritis": ["swelling_joints", "movement_stiffness", "loss_of_balance"],
    "Paroymsal Positional Vertigo": ["dizziness", "unsteadiness", "loss_of_balance"],
    "Acne": ["blackheads", "small_dents_in_nails", "inflammatory_nails"],
    "Urinary tract infection": ["internal_itching", "toxic_look_(typhos)", "depression"],
    "Psoriasis": ["red_spots_over_body", "watering_from_eyes", "increased_appetite"],
    "Hepatitis D": ["muscle_pain", "altered_sensorium", "red_spots_over_body"],
    "Hepatitis B": ["belly_pain", "abnormal_menstruation", "dischromic _patches"],
    "Allergy": ["watering_from_eyes", "increased_appetite", "mucoid_sputum"],
    "Hepatitis A": ["red_spots_over_body", "watering_from_eyes", "increased_appetite"],
    "GERD": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Chronic cholestasis": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Drug Reaction": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Peptic ulcer disease": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "AIDS": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Diabetes": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Gastroenteritis": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Bronchial Asthma": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Hypertension": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Migraine": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Cervical spondylosis": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Paralysis (brain hemorrhage)": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Jaundice": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Malaria": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Chicken pox": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Dengue": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Typhoid": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Impetigo": ["family_history", "mucoid_sputum", "rusty_sputum"],
    "Diabetes Prediction": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"],
    "Heart Disease Prediction": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
}

# Set the paths for your models
diabetes_model_path = 'C:/Users/sudha/Downloads/Disease prediction/Diabetes Prediction/Diabetes prediction bot trained_model.sav'
heart_disease_model_path = 'C:/Users/sudha/Downloads/Disease prediction/Heart Disease prediction/Heart disease prediction bot trained_model.sav'

# Loading the saved models
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        "PolyDisease Predictor",
        ["🩸 Diabetes Prediction", "❤️ Heart Disease Prediction", "🦠 Multiple Disease Prediction"],
    )

# Diabetes Prediction Page
if selected == "🩸 Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    # Input fields
    pregnancies = st.number_input("Number of Pregnancies")
    glucose = st.number_input("Glucose Level")
    blood_pressure = st.number_input("Blood Pressure value")
    skin_thickness = st.number_input("Skin Thickness value")
    insulin = st.number_input("Insulin Level")
    bmi = st.number_input("BMI value")
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function value")
    age = st.number_input("Age of the Person")

 # Debugging line: Add this line to print out variable values
    st.write("Debug: pregnancies =", pregnancies)
    
    # Prediction button
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict(
            [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
        )
        diab_diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == "❤️ Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")

    # Input fields
    age = st.number_input("Age")
    sex = st.number_input("Sex")
    cp = st.number_input("Chest Pain types")
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Serum Cholestoral in mg/dl")
    fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")
    restecg = st.number_input("Resting Electrocardiographic results")
    thalach = st.number_input("Maximum Heart Rate achieved")
    exang = st.number_input("Exercise Induced Angina")
    oldpeak = st.number_input("ST depression induced by exercise")
    slope = st.number_input("Slope of the peak exercise ST segment")
    ca = st.number_input("Major vessels colored by flourosopy")
    thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    # Prediction button
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        )
        heart_diagnosis = "The person is having heart disease" if heart_prediction[0] == 1 else "The person does not have any heart disease"
        st.success(heart_diagnosis)

# Multiple Disease Prediction Page
if selected == "🦠 Multiple Disease Prediction":
    st.title("Multiple Disease Prediction using Symptoms")

    # User input for symptoms
    symptoms = st.text_input("Enter Symptoms (comma-separated)")

    # Initialize the result
    diagnosis = ''

    # Create a button to check symptoms
    if st.button("Check Symptoms"):
        # Call the symptomPrediction function with user input
        diseases = symptomPrediction(symptoms, disease_data)
        if diseases:
            diagnosis = f"Possible Diseases: {', '.join(diseases)}"
        else:
            diagnosis = "No matching diseases found for the given symptoms."

    st.success(diagnosis)
