# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:04:19 2023

@author: sudha
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Function to predict diseases based on symptoms
def predict_diseases(symptoms):
    # Creating input data for the model
    input_data = [0] * len(features.columns)
    for symptom in symptoms:
        if symptom in features.columns:
            index = features.columns.get_loc(symptom)
            input_data[index] = 1

    # Reshaping the input data
    input_data = pd.DataFrame([input_data], columns=features.columns)

    # Generating predictions
    predictions = rf.predict(input_data)
    return predictions

# Load data
train_data = pd.read_csv('Multiple disease prediction/Training.csv')
test_data = pd.read_csv('Multiple disease prediction/Testing.csv')

# Split data into features and target variable
features = train_data.drop('prognosis', axis=1)
target = train_data['prognosis']

# Create RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)

# Train the model
rf.fit(features, target)

# Streamlit app
st.title("Multiple Disease Prediction using Symptoms")

# User input for symptoms
symptoms = st.text_input("Enter Symptoms (comma-separated)")

# Initialize the result
diagnosis = ''

# Create a button to check symptoms
if st.button("Check Symptoms"):
    # Call the predict_diseases function with user input
    diseases = predict_diseases(symptoms.split(","))
    st.success(f"Predicted Diseases: {', '.join(diseases)}")
