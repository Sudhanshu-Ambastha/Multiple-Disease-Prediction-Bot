# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 07:48:04 2023

@author: sudha
"""

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import pickle
from streamlit_option_menu import option_menu

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

# Initialize the symptom-to-index mapping
symptom_index = {symptom: index for index, symptom in enumerate(sorted(set(symptom for symptoms in disease_data.values() for symptom in symptoms)))}

# Initialize the symptom encoder
encoder = LabelEncoder()

# Read the training data
DATA_PATH = 'C:/Users/sudha/Downloads/Disease prediction/Multiple disease prediction/Training.csv'
data = pd.read_csv(DATA_PATH).dropna(axis=1)

# Encoding the target values
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

# Initialize Models
models = {
    "SVC": SVC(),
    "Gaussian NB": GaussianNB(),
    "Random Forest": RandomForestClassifier(random_state=18)
}

# Train and test the models
svm_model = SVC()
svm_model.fit(X_train, y_train)
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(X_train, y_train)

# Combine the models
final_svm_model = SVC()
final_nb_model = GaussianNB()
final_rf_model = RandomForestClassifier(random_state=18)
final_svm_model.fit(X, y)
final_nb_model.fit(X, y)
final_rf_model.fit(X, y)

# Read the test data
test_data = pd.read_csv('C:/Users/sudha/Downloads/Disease prediction/Multiple disease prediction/Testing.csv').dropna(axis=1)
test_X = test_data.iloc[:, :-1]
test_Y = encoder.transform(test_data.iloc[:, -1])

# Create a Streamlit app
def main():
    st.title("PolyDisease Predictor")

    # User input for symptoms
    symptoms = st.text_input("Enter Symptoms (comma-separated)")

    # Initialize the result for both systems
    disease_diagnosis = ''
    symptom_diagnosis = ''

    # Create a button for symptom prediction
    if st.button("Check Symptoms"):
        # Call the symptomPrediction function with user input
        diseases = symptomPrediction(symptoms, disease_data)
        if diseases:
            symptom_diagnosis = f"Possible Diseases: {', '.join(diseases)}"
        else:
            symptom_diagnosis = "No matching diseases found for the given symptoms."

    # Create a button for disease prediction
    if st.button("Disease Prediction"):
        # Call the diseasePrediction function with user input
        disease_name = diseasePrediction(symptoms, disease_data)
        disease_diagnosis = f"Disease Found: {disease_name}"

    st.success(symptom_diagnosis)
    st.success(disease_diagnosis)

# Defining the Function to make predictions for disease classification
def diseasePrediction(symptoms, disease_data):
    input_symptoms = set(symptoms.split(","))
    for disease, disease_symptoms in disease_data.items():
        if input_symptoms == set(disease_symptoms):
            return disease
    return "No diseases found"

# Defining the Function to check symptoms and suggest possible diseases
def symptomPrediction(symptoms, disease_data):
    input_symptoms = set(symptoms.split(","))
    possible_diseases = []

    for disease, disease_symptoms in disease_data.items():
        print(f"Comparing {input_symptoms} with {disease_symptoms}")
        if input_symptoms == set(disease_symptoms):
            possible_diseases.append(disease)

    return possible_diseases



if __name__ == '__main__':
    main()

