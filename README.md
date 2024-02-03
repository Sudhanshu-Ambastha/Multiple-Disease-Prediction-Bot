# Multiple Disease Prediction Bot

![Web capture_16-12-2023_15579_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/22a87cc6-fc4d-4ed5-832d-dd8d9d230f94)
![Web capture_16-12-2023_16327_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/5a297e58-7ead-4407-8116-bdfff8585079)

## Table of Contents

- [About](#about)
- [Files](#files)
- [Features](#features)
- [Usage](#usage)

## About

The Multiple Disease Prediction Bot is a machine learning model designed to predict up to 40 different diseases based on input symptoms. The model is trained on a dataset with approximately 131 parameters and utilizes three different training models: Support Vector Machine (SVM), Random Forest (RF), and Naive Bayes (NB).

Please note that when providing input to the bot, it's important to format the symptoms as follows: "Itching,Skin_Rash,Nodal_Skin_Eruptions." Incorrect formatting may lead to false predictions or errors.

## Files

1. **Multiple disease prediction with spyder.py (working main model):** This file contains the main code for the disease prediction bot using the Spyder IDE.
2. **Multiple_disease_prediction_bot_trained_model_svm.sav:** This file contains the trained SVM model for disease prediction.
3. **Testing.csv:** The dataset used for testing the disease prediction bot.
4. **Training.csv:** The dataset used for training the machine learning models.
5. **multiple_disease_prediction_.py (Google Colab file):** The Google Colab file for disease prediction using the trained models.

## Features

- Predicts up to 40 different diseases.
- Utilizes approximately 131 to 133 parameters for training.
- Trained on three different models: SVM, RF, and NB.

## Usage

To use the Multiple Disease Prediction Bot, follow these steps:

1. Open the "Multiple disease prediction with spyder.py" file using an appropriate IDE like Spyder.
2. Format the input symptoms as "Itching,Skin_Rash,Nodal_Skin_Eruptions."
3. Run the code to get disease predictions.

Remember to ensure that the input is properly formatted to receive accurate predictions.

### Format for Input Parameters

When providing input parameters for disease prediction, use the following format: "Parameter1,Parameter2,Parameter3."

### Available Diseases and Parameters

- **Fungal infection:** Itching,Skin_Rash,Nodal_Skin_Eruptions
- **Hepatitis C:** Continuous_Sneezing,Shivering,Chills
- **Hepatitis E:** Joint_Pain,Stomach_Pain,Acidity
- **Alcoholic hepatitis:** Ulcers_on_Tongue,Muscle_Wasting,Vomiting
- **Tuberculosis:** Cough,High_Fever,Sweating
- **Common Cold:** Continuous_Sneezing,Chills,Fatigue
- **Pneumonia:** High_Fever,Sweating,Breathlessness
- **Dimorphic hemmorhoids(piles):** Bleeding,Pain_During_Bowel_Movements,Bloody_Stool
- **Heart attack:** Chest_Pain,Weakness_in_Limbs,Fast_Heart_Rate
- **Varicose veins:** Swollen_Legs,Swollen_Blood_Vessels,Puffy_Face_and_Eyes
- **Hypothyroidism:** Fatigue,Weight_Gain,Cold_Hands_and_Feets
- **Hyperthyroidism:** Mood_Swings,Weight_Loss,Restlessness
- **Hypoglycemia:** Lethargy,Patches_in_Throat,Irregular_Sugar_Level
- **Osteoarthristis:** Pain_in_Joints,Muscle_Weakness,Stiff_Neck
- **Arthritis:** Swelling_Joints,Movement_Stiffness,Loss_of_Balance
- **Paroymsal Positional Vertigo:** Dizziness,Unsteadiness,Loss_of_Balance
- **Acne:** Blackheads,Small_Dents_in_Nails,Inflammatory_Nails
- **Urinary tract infection:** Internal_Itching,Toxic_Look_(Typhos),Depression
- **Psoriasis:** Red_Spots_Over_Body,Watering_From_Eyes,Increased_Appetite
- **Hepatitis D:** Muscle_Pain,Altered_Sensorium,Red_Spots_Over_Body
- **Hepatitis B:** Belly_Pain,Abnormal_Menstruation,Dischromic_Patches
- **Allergy:** Watering_From_Eyes,Increased_Appetite,Mucoid_Sputum
- **Hepatitis A:** Red_Spots_Over_Body,Watering_From_Eyes,Increased_Appetite
- **GERD:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Chronic cholestasis:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Drug Reaction:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Peptic ulcer disease:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **AIDS:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Diabetes:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Gastroenteritis:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Bronchial Asthma:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Hypertension:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Migraine:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Cervical spondylosis:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Paralysis (brain hemorrhage):** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Jaundice:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Malaria:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Chicken pox:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Dengue:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Typhoid:** Family_History,Mucoid_Sputum, Rusty_Sputum
- **Impetigo:** Family_History,Mucoid_Sputum,Rusty_Sputum
- **Diabetes Prediction:** For diabetes prediction, provide the following parameters - Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
- **Heart Disease Prediction:** For heart disease prediction, provide the following parameters - Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thal,Exang,OldPeak,Slope,Ca,Thal

Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

### Getting Disease Predictions

To get a prediction for a specific disease, simply copy and paste the parameters for that disease in the format mentioned above. The model will analyze the input parameters and provide a prediction for the disease based on the provided data.

Remember to include all relevant parameters in the input to receive accurate predictions.

## Troubleshooting
If you encounter any issues or have questions, please don't hesitate to reach out for support.

Happy predicting! 🤖💙

## Author  
@Sudhanshu-Ambastha

