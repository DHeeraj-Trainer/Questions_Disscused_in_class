import random
import pandas as pd
from faker import Faker

fake = Faker()

# Columns for the dataframe
columns = [
    "Patient_ID", "Age", "Gender", "Medical_History",
    "Visit_ID", "Visit_Date", "Diagnoses", "Lab_Results", "Medications",
    "Smoking_Status", "Alcohol_Consumption", "Exercise_Frequency", "Diet_Type",
    "Chronic_Disease_Risk", "Readmission_Probability",
    "Occupation", "Marital_Status", "Education_Level", "Income_Level", "Region",
    "Family_History", "Social_Support", "Sleep_Habits", "Stress_Level", "Healthcare_Access"
]

# Simulating data for 10,000 patients
data = []
for i in range(10000):
    patient_id = f"P00{i+1}"
    age = random.randint(18, 90)
    gender = random.choice(["Male", "Female", "Other"])
    medical_history = random.choice(["Hypertension, Diabetes", "Asthma", "None", "Diabetes", "Hypertension"])
    visit_id = f"V00{i+1}"
    visit_date = fake.date_this_year()
    diagnoses = random.choice(["Hypertension", "Diabetes", "Asthma", "None"])
    lab_results = f"BP: {random.randint(110, 150)}/{random.randint(70, 100)}, Cholesterol: {random.randint(180, 250)} mg/dL"
    medications = random.choice(["Amlodipine, Metformin", "Salbutamol", "None", "Metformin", "Amlodipine"])
    smoking_status = random.choice(["Yes", "No"])
    alcohol_consumption = random.choice(["None", "Occasional", "Regular"])
    exercise_frequency = random.choice(["Daily", "Weekly", "Rarely"])
    diet_type = random.choice(["Vegetarian", "Non-Vegetarian", "Vegan"])
    chronic_disease_risk = random.randint(30, 90)
    readmission_probability = round(random.uniform(0, 1), 2)
    occupation = random.choice(["Engineer", "Teacher", "Student", "Retired", "Doctor"])
    marital_status = random.choice(["Married", "Single", "Widowed"])
    education_level = random.choice(["High School", "Undergraduate", "Graduate", "Postgraduate"])
    income_level = random.choice(["Low", "Middle", "High"])
    region = random.choice(["Maharashtra", "Punjab", "Karnataka", "Kerala", "Tamil Nadu"])
    family_history = random.choice(["Diabetes, Heart Disease", "Asthma", "None"])
    social_support = random.choice(["High", "Medium", "Low"])
    sleep_habits = random.choice([5, 6, 7, 8])
    stress_level = random.randint(1, 10)
    healthcare_access = random.choice(["Monthly", "Quarterly", "Rarely"])

    # Add all fields as a row in data list
    row = [patient_id, age, gender, medical_history,
           visit_id, visit_date, diagnoses, lab_results, medications,
           smoking_status, alcohol_consumption, exercise_frequency, diet_type,
           chronic_disease_risk, readmission_probability,
           occupation, marital_status, education_level, income_level, region,
           family_history, social_support, sleep_habits, stress_level, healthcare_access]
    data.append(row)

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("patient_data.csv", index=False)

print("Data has been successfully generated and saved to 'patient_data.csv'.")
