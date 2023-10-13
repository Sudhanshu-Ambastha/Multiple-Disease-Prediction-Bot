# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

from tkinter import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

# List of symptoms (excluding the ones not in your dataset)
l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
      'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
      'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
      'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness',
      'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
      'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
      'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes',
      'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
      'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
      'dizziness', 'cramps', 'bruising', 'obesity', 'puffy_face_and_eyes',
      'enlarged_thyroid', 'brittle_nails', 'excessive_hunger', 'extra_marital_contacts',
      'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
      'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'continuous_feel_of_urine',
      'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
      'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'watering_from_eyes',
      'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
      'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
      'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum',
      'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads',
      'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
      'red_sore_around_nose', 'yellow_crust_ooze']

# List of diseases
disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer disease',
           'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', 'Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins', 'Hypothyroidism',
           'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroxysmal Positional Vertigo',
           'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']

l2 = [0] * len(l1)

# Load your training data
df = pd.read_csv("C://Users//sudha//Downloads//Disease prediction//Multiple disease prediction//Training.csv")

# Encode the target labels if they are not already numeric
label_encoder = LabelEncoder()
df["prognosis"] = label_encoder.fit_transform(df["prognosis"])

X = df[l1]
y = df["prognosis"]

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier and fit it to the data
clf_dt = DecisionTreeClassifier()
clf_dt.fit(X_train, y_train)

# Create a Random Forest Classifier and fit it to the data
clf_rf = RandomForestClassifier()
clf_rf.fit(X_train, y_train)

# Create a Naive Bayes classifier and fit it to the data
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# ... (Rest of the code remains the same)
# ... (Previous code remains the same)

# Predictions using the Decision Tree Classifier
y_pred_dt = clf_dt.predict(X_test)

# Predictions using the Random Forest Classifier
y_pred_rf = clf_rf.predict(X_test)

# Predictions using the Naive Bayes Classifier
y_pred_nb = gnb.predict(X_test)

# Calculate and print the accuracy for each classifier
accuracy_dt = accuracy_score(y_test, y_pred_dt)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_nb = accuracy_score(y_test, y_pred_nb)

print("Decision Tree Classifier Accuracy:", accuracy_dt)
print("Random Forest Classifier Accuracy:", accuracy_rf)
print("Naive Bayes Classifier Accuracy:", accuracy_nb)

# Function to predict the disease based on symptoms
def predict_disease(symptoms):
    # Create a dictionary to map symptoms to their indices in the feature list
    symptom_to_index = {symptom: index for index, symptom in enumerate(l1)}
    
    # Create a numpy array to hold the input symptoms
    input_data = np.zeros(len(l1))
    
    # Set the indices corresponding to the input symptoms to 1
    for symptom in symptoms:
        if symptom in symptom_to_index:
            input_data[symptom_to_index[symptom]] = 1
    
    # Predict the disease using the Decision Tree Classifier
    disease_dt = label_encoder.inverse_transform([clf_dt.predict([input_data])])[0]
    
    # Predict the disease using the Random Forest Classifier
    disease_rf = label_encoder.inverse_transform([clf_rf.predict([input_data])])[0]
    
    # Predict the disease using the Naive Bayes Classifier
    disease_nb = label_encoder.inverse_transform([gnb.predict([input_data])])[0]
    
    return {
        "Decision Tree Classifier": disease_dt,
        "Random Forest Classifier": disease_rf,
        "Naive Bayes Classifier": disease_nb
    }

# Example usage of the predict_disease function
input_symptoms = ['itching', 'skin_rash', 'chills', 'muscle_wasting', 'fatigue']
predicted_diseases = predict_disease(input_symptoms)

print("Predicted Diseases for Input Symptoms:", input_symptoms)
for classifier, disease in predicted_diseases.items():
    print(f"{classifier}: {disease}")

# Deployment starts

def main():
    
    
   add_text = input("Do you want to add text? (y/n): ")

if add_text == "y":
    text_to_add = input("Enter the text you want to add: ")
    st.text(text_to_add)  # Add the text to Streamlit
else:
    st.title("Disease Prediction App")
    st.write("Enter your symptoms and get disease predictions.")

    symptom1 = st.selectbox("Symptom 1", l1)
    symptom2 = st.selectbox("Symptom 2", l1)
    symptom3 = st.selectbox("Symptom 3", l1)
    symptom4 = st.selectbox("Symptom 4", l1)
    symptom5 = st.selectbox("Symptom 5", l1)

    if st.button("Predict"):
        symptoms = [symptom1, symptom2, symptom3, symptom4, symptom5]
        predicted_disease = predict_disease(symptoms)  # Call your prediction function here
        st.write(f"Predicted Disease: {predicted_disease}")





if __name__ == '__main__':
    main()


