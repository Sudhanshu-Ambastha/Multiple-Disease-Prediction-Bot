# Multiple Disease Prediction Bot

![Web capture_16-12-2023_15579_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/22a87cc6-fc4d-4ed5-832d-dd8d9d230f94)
![Web capture_16-12-2023_16327_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/5a297e58-7ead-4407-8116-bdfff8585079)

## Table of Contents

- [About](#about)
- [Files](#files)
- [Features](#features)
- [Usage](#usage)

## About

The Multiple Disease Prediction Bot is a machine learning model designed to predict up to 41 different diseases based on input symptoms. The model is trained on a dataset with approximately 131 parameters and utilizes three different training models: Support Vector Machine (SVM), Random Forest (RF), and Naive Bayes (NB).

Please note that when providing input to the bot, it's important to format the symptoms as follows: "Itching, Skin Rash, Nodal Skin Eruptions" Incorrect formatting may lead to false predictions or errors.

## Files

1.  **`LabelEncoder.ipynb`:** Jupyter Notebook likely used for encoding categorical disease labels.
2.  **`Multiple disease prediction with spyder.py`:** The main Python script for the disease prediction bot, likely intended to be run with Spyder IDE.
3.  **`Multiple_Disease_prediction_.ipynb`:** Jupyter Notebook for disease prediction, potentially used in Google Colab.
4.  **`Multiple_disease_prediction_bot_trained_model.sav`:** The serialized (saved) trained Support Vector Machine (SVM) model.
5.  **`README.md`:** This file, providing information about the project.
6.  **`Testing.csv`:** The dataset used for evaluating the performance of the trained model.
7.  **`Training.csv`:** The dataset used for training the machine learning model.
8.  **`label_encoder.sav`:** The serialized (saved) LabelEncoder object, used to transform disease names.
9.  **`multiple_disease_prediction.py`:** Another Python script for disease prediction, potentially a refactored or alternative version.

## Features

- Predicts up to 41 different diseases.
- Utilizes approximately 131 parameters for training.
- Trained on three different models: SVM, RF, and NB.

## Usage

To use the Multiple Disease Prediction Bot, follow these steps:

1. Open the "Multiple disease prediction with spyder.py" file using an appropriate IDE like Spyder.
2. Ensure that the necessary dependencies are installed, including the required Python libraries.
```
pip install matplotlib seaborn scikit-learn numpy pandas scipy
```
3. Format the input symptoms as "Itching, Skin Rash, Nodal Skin Eruptions"
4. Run the code to get disease predictions.
```
& "C:\Users\sudha\AppData\Roaming\Python\Python313\Scripts\streamlit.exe" run "Multiple disease prediction with spyder.py"
```
or
```
streamlit run Multiple disease prediction with spyder.py
```

Remember to ensure that the input is properly formatted to receive accurate predictions.

### Format for Input Parameters

When providing input parameters for disease prediction, use the following format: "Parameter1,Parameter2,Parameter3.
"for ex= "**Fungal infection:** Itching, Skin Rash, Nodal Skin Eruptions"

# List of Available Symptoms & Diseases
<details>
<summary>List of Symptoms:-</summary>

|A|B|C|D|E|
|---|---|---|---|---|
|Abnormal_Menstruation|Bladder_Discomfort|Chest_Pain|Dark_Urine|Enlarged_Thyroid|  
|Abdominal_Pain|Belly_Pain|Chills|Dehydration|Excessive_Hunger| 
|Acidity|Blurred_And_Distorted_Vision|Cold_Hands_and_Feets|Depression|Extra_Marital_Contacts|
|Acute_Liver_Failure|Bloody_Stool|Coma|Diarrhoea|
|Altered_Sensorium|Back_Pain|Constipation|Dizziness| 
|Anxiety|Breathlessness|Congestion|Drying_and_Tingling_Lips| 
||Belly_Pain|Continuous_Sneezing|Dischromic|  
||Brittle_Nails|Continuous_Feel_of_Urine|Distention_Of_Abdomen|
||Blackheads|Cough|
||Bruising|Cramps|
||Blister 
||Burning_Micturition| 
||Blood_In-Sputum|

|F|H|I|J|K|L|
|---|---|---|---|---|---|
|Fast_Heart_Rate|High_Fever|Irregular_Sugar_Level|Joint_Pain|Knee_Pain|Lack_of_Concentration|  
|Fatigue|Headache|Increased_Appetite |||Lethargy|  
|Fluid_Overload|Hip_Joint_Painlurred_And_Distorted_Vision|Increased_Urination|||Loss_of_Appetite|
|Foul_Smell_of_Urine|History_of_Alcohol_Consumption|Indigestion|||Loss_of_Balance|
|Family-History||Inflammatory_Nails |||Loss_of_Smell|
|||Internal_Itching|| 
|||Irritability||  
|||Irritation_in_Anus||
|||Itching|

|M|N|O|P|R|S|
|---|---|---|---|---|---|
|Muscle_Wasting|Nausea|Obesity|Phlegm|Redness_Of_Eyes|Slurred_Speech| 
|Malaise|Neck_Pain||Pain_Behind_The_Eyes|Red_Sore_Around_Nose|Sweating| 
|Metallic_Taste|Nodal_Skin_Eruptions||Patches_In_Throat|Red_Spots_Over_Body|Sunken_Eyes|
|Mild_Fever|||Pain_During_Bowel_Movements|Restlessness|Scurring|
|Mood_Swings|||Pain_in_Anal_Region|Runny_Nose|Shivering|  
|Movement_Stiffness|||Painful_Walking|Rusty_Sputum|Silver_Like_Dusting|  
|Muscle_Pain|||Palpitations|Receiving_blood_transfusion|Sinus_Pressure| 
|Muscle_Weakness|||Polyuria|Receiving_Unterile_Injections|Skin_Peeling|
|Muscular_Stiffness|||Prominent_Veins_on_Calf||Skin_Rash|
|Mucoid_Sputum|||Puffy_Face_and_Eyes||Small_Dents_in_Nails|  
||||Pus_Filled_Pimples||Spinning_Movements|
||||Patches||Spotting_Urination|
||||Palpitations||Stiff_Neck|
||||||Stomach_Pain|     
||||||Stomach_Bleeding| 
||||||Swelling_Joints| 
||||||Swelling_of_Stomach|  
||||||Swollen_Legs| 
||||||Swollen_Blood_Vessels| 
||||||Swollen_Extremities| 
||||||Swollen_Lymph_Nodes| 

|T|U|V|W|Y|
|---|---|---|---|---|
|Throat_Irritation|Ulcers_on_Tongue|Vomiting|Watering_From_Eyes|Yellow_Crust_Ooze|  
|Toxic_Look_(Typhos)|Unsteadiness|Visual-Disturbances|Weakness_in_Limbs|Yellow_Urine| 
||||Weight_Gain|Yellowing_of_Eyes |
||||Weight_Loss|Yellowish_Skin |
||||weakness_of_one_body_side||
</details>
<details>
<summary>List of Diseases:-</summary>
    
| Column 1                   | Column 2                   | Column 3               | Column 4                   | Column 5               |
|----------------------------|----------------------------|------------------------|----------------------------|------------------------|
| Fungal infection           | Jaundice                   | Heart attack           | Arthritis                  | GERD                   |
| Hepatitis C                | Malaria                    | Varicose veins         | Paroymsal Positional Vertigo | Diabetes             |
| Hepatitis E                | Pneumonia                  | Gastroenteritis        | Acne                       | Heart Disease          |
| Alcoholic hepatitis        | Dengue                     | Bronchial Asthma       | Urinary tract infection    | Chronic cholestasis    |
| Tuberculosis               | Typhoid                    | Hypoglycemia           | Psoriasis                  | Drug Reaction          |
| Common Cold                | Hypothyroidism             | Osteoarthristis        | Hepatitis D                | Peptic ulcer disease   |
| Chicken pox                | Hyperthyroidism            | Migraine               | Hepatitis B                | AIDS                   |
| Dimorphic hemmorhoids(piles)| Hypertension              | Paralysis (brain hemorrhage) | Allergy              | Hepatitis A            |
| Impetigo                   |                            |                        |                            |                        |
</details>

### Getting Disease Predictions

To get a disease prediction, you need to run one of the provided Python scripts or notebooks. The input format for symptoms is a comma-separated string.

**Example Input:** `"Itching,Skin_Rash,Nodal_Skin_Eruptions"`

The model will analyze the provided symptoms and output a predicted disease. Ensure you provide a sufficient number of relevant symptoms for a more accurate prediction.

## Troubleshooting
If you encounter any issues or have questions, please don't hesitate to reach out for support.

Happy predicting! 🤖💙

## Check out the other repositories related to this one
<details>
<summary>Related Repos which you should check out:-</summary>

![Web capture_16-12-2023_162935_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/b33c540d-9cb2-410c-b83c-37b99be726de)  
- [Diabetes Prediction Bot](https://github.com/Sudhanshu-Ambastha/Diabetes-Prediction-Bot)

![Web capture_16-12-2023_162351_localhost](https://github.com/Sudhanshu-Ambastha/Google-background/assets/135802131/10dc50a7-ac7d-4972-bf52-736f448a6ca4)  
- [Heart Disease Prediction Bot](https://github.com/Sudhanshu-Ambastha/Heart-Disease-Prediction-Bot)

</details>
- Check out the main repo as this project is part of it

[Combined Disease Predictor](https://github.com/Sudhanshu-Ambastha/Combined-Disease-Prediction-Bot)

## Contributors
<table>
    <tr>
        <td align="center">
        <a href="http://github.com/Sudhanshu-Ambastha">
            <img src="https://avatars.githubusercontent.com/u/135802131?v=4" width="100px;" alt=""/>
            <br />
            <sub><b>Sudhanshu Ambastha </b></sub>
        </a>
        <br />
    </td>
    <td align="center">
        <a href="https://github.com/Vishwas567917">
            <img src="https://avatars.githubusercontent.com/u/139749696?s=100&v=4" width="100px;" alt=""/>
            <br />
            <sub><b>Parth Shrivastava</b></sub>
        </a>
        <br />
    </td>
    <td align="center">
        <a href="https://github.com/Sarthak966829">
            <img src="https://avatars.githubusercontent.com/u/139750289?s=100&v=4" width="100px;" alt=""/>
            <br />
            <sub><b>Sarthak Srivastava</b></sub>
        </a>
        <br />
    </td>
    </tr>
</table>
