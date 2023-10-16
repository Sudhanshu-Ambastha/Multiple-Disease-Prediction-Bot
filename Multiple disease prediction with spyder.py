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


def symptomPrediction(symptoms, disease_data):
    input_symptoms = set(symptoms.lower().split(","))
    possible_diseases = []

    for disease, disease_symptoms in disease_data.items():
        if input_symptoms == set(symptom.lower() for symptom in disease_symptoms):
            possible_diseases.append(disease)

    return possible_diseases

# Create a Streamlit app
def main():
    st.title("Disease Predictor")

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

if __name__ == '__main__':
    main()
