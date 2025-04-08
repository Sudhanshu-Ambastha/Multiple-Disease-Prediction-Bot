import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- Load Trained Combined Model ---
try:
    combined_model = joblib.load('./Multiple_disease_prediction_bot_trained_model.sav')
except FileNotFoundError:
    st.error("Error loading the combined model file ('./Multiple_disease_prediction_bot_trained_model.sav'). Please ensure it's in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while loading the combined model: {e}")
    st.stop()

# --- Load Trained LabelEncoder ---
try:
    label_encoder = joblib.load('./label_encoder.sav')
except FileNotFoundError:
    st.error("Error loading the LabelEncoder file ('./label_encoder.sav'). Please ensure it's in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while loading the LabelEncoder: {e}")
    st.stop()

# --- Load Training Data to Get Features ---
try:
    train_data = pd.read_csv('./Training.csv')
    features_columns = train_data.drop('prognosis', axis=1).columns
except FileNotFoundError:
    st.error("Error loading 'Training.csv'. Please ensure it's in the same directory as the app.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while loading 'Training.csv': {e}")
    st.stop()

# --- Prediction Function ---
def predict_diseases(symptoms_str):
    symptoms = [s.strip().capitalize() for s in symptoms_str.split(',')]
    input_data = pd.DataFrame(np.zeros((1, len(features_columns)), dtype=int), columns=features_columns)
    for symptom in symptoms:
        symptom_lower_no_space = symptom.lower().replace(' ', '_')
        if symptom_lower_no_space in features_columns:
            input_data[symptom_lower_no_space] = 1

    prediction_encoded = combined_model.predict(input_data)[0]
    predicted_disease = label_encoder.inverse_transform([prediction_encoded])[0]
    return predicted_disease

# --- Streamlit App Layout ---
st.title("Multiple Disease Prediction System")

symptoms_input = st.text_area("Enter your symptoms (comma-separated):", placeholder="e.g., Itching, Skin Rash, Nodal Skin Eruptions")

predict_button = st.button("Predict Disease")

if predict_button and symptoms_input:
    if symptoms_input.strip():
        try:
            predicted_disease = predict_diseases(symptoms_input)
            st.success(f"Predicted Disease: {predicted_disease}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please enter some symptoms.")

st.markdown("---")
st.markdown("Developed By Sudhanshu Ambastha.")