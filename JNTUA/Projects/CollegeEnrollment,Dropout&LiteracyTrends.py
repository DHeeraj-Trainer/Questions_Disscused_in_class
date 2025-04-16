import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define lists for categorical data
states = ['Andhra Pradesh', 'Bihar', 'Telangana', 'Karnataka', 'Maharashtra', 'Tamil Nadu', 'Uttar Pradesh', 'West Bengal', 'Rajasthan', 'Punjab', 'Haryana']
gender = ['Male', 'Female', 'Other']
course_types = ['UG', 'PG', 'Vocational']
reasons_for_dropout = ['Financial', 'Personal', 'Academic', 'Other']
digital_access = ['Yes', 'No']
regions = ['Urban', 'Rural']

# State-specific characteristics for generating data (Example: Larger states have more enrollments)
state_characteristics = {
    'Andhra Pradesh': {'min_enrollment': 1000, 'max_enrollment': 25000, 'dropout_rate': 10},
    'Bihar': {'min_enrollment': 500, 'max_enrollment': 15000, 'dropout_rate': 15},
    'Telangana': {'min_enrollment': 1000, 'max_enrollment': 20000, 'dropout_rate': 12},
    'Karnataka': {'min_enrollment': 1500, 'max_enrollment': 30000, 'dropout_rate': 8},
    'Maharashtra': {'min_enrollment': 2000, 'max_enrollment': 50000, 'dropout_rate': 6},
    'Tamil Nadu': {'min_enrollment': 1500, 'max_enrollment': 25000, 'dropout_rate': 9},
    'Uttar Pradesh': {'min_enrollment': 5000, 'max_enrollment': 60000, 'dropout_rate': 18},
    'West Bengal': {'min_enrollment': 1500, 'max_enrollment': 25000, 'dropout_rate': 11},
    'Rajasthan': {'min_enrollment': 1000, 'max_enrollment': 20000, 'dropout_rate': 13},
    'Punjab': {'min_enrollment': 1000, 'max_enrollment': 15000, 'dropout_rate': 7},
    'Haryana': {'min_enrollment': 800, 'max_enrollment': 15000, 'dropout_rate': 10}
}

# Generate data for different categories

# 1. State-wise Data
num_rows = 10000
state_data = {
    'State': [random.choice(states) for _ in range(num_rows)],
    'Year': np.random.randint(2010, 2024, size=num_rows),
    'Number_of_Enrollments': [0] * num_rows,  # Pre-allocate lists with default values
    'UG_Enrollments': [0] * num_rows,
    'PG_Enrollments': [0] * num_rows,
    'Vocational_Enrollments': [0] * num_rows,
    'Gender_Breakdown_Male': np.random.randint(0, 50000, size=num_rows),
    'Gender_Breakdown_Female': np.random.randint(0, 50000, size=num_rows),
    'Gender_Breakdown_Other': np.random.randint(0, 5000, size=num_rows),
    'Dropout_Count': [0] * num_rows,
    'Dropout_Percentage': np.random.uniform(0, 100, size=num_rows),
    'Reason_for_Dropout_Financial': np.random.randint(0, 5000, size=num_rows),
    'Reason_for_Dropout_Personal': np.random.randint(0, 5000, size=num_rows),
    'Reason_for_Dropout_Academic': np.random.randint(0, 5000, size=num_rows),
    'Reason_for_Dropout_Other': np.random.randint(0, 5000, size=num_rows),
    'Literacy_Rate': np.random.uniform(50, 100, size=num_rows),
    'Male_Literacy_Rate': np.random.uniform(50, 100, size=num_rows),
    'Female_Literacy_Rate': np.random.uniform(50, 100, size=num_rows),
    'Urban_Literacy_Rate': np.random.uniform(50, 100, size=num_rows),
    'Rural_Literacy_Rate': np.random.uniform(50, 100, size=num_rows),
    'Student_Teacher_Ratio': np.random.uniform(5, 30, size=num_rows),
    'Infrastructure_Score': np.random.randint(1, 6, size=num_rows),
    'Digital_Access': np.random.choice(digital_access, size=num_rows),
    'School_Dropout_Rate': np.random.uniform(0, 100, size=num_rows),
    'College_Dropout_Rate': np.random.uniform(0, 100, size=num_rows),
    'Vocational_Education_Enrollment': np.random.randint(100, 5000, size=num_rows),
    'Gender_Parity_Index': np.random.uniform(0, 1, size=num_rows),
    'Rural_vs_Urban_Enrollment': np.random.uniform(0, 100, size=num_rows),
    'Financial_Support_Programs': np.random.randint(0, 10000, size=num_rows),
    'Educational_Quality_Index': np.random.uniform(1, 10, size=num_rows)
}

# Adjust values based on state characteristics
for i in range(num_rows):
    state = state_data['State'][i]
    state_info = state_characteristics[state]
    min_enrollment = state_info['min_enrollment']
    max_enrollment = state_info['max_enrollment']
    dropout_rate = state_info['dropout_rate']
    
    # Generate enrollment data based on state-specific characteristics
    state_data['Number_of_Enrollments'][i] = np.random.randint(min_enrollment, max_enrollment)
    state_data['UG_Enrollments'][i] = np.random.randint(min_enrollment // 10, max_enrollment // 2)
    state_data['PG_Enrollments'][i] = np.random.randint(min_enrollment // 20, max_enrollment // 5)
    state_data['Vocational_Enrollments'][i] = np.random.randint(min_enrollment // 50, max_enrollment // 10)
    
    # Generate dropout data based on dropout rate of the state
    state_data['Dropout_Count'][i] = int(state_data['Number_of_Enrollments'][i] * (dropout_rate / 100))
    state_data['Dropout_Percentage'][i] = dropout_rate

# 2. User Data
user_data = {
    'User_ID': [fake.uuid4() for _ in range(num_rows)],
    'Age': np.random.randint(18, 65, size=num_rows),
    'Gender': np.random.choice(gender, size=num_rows),
    'Location': [fake.city() for _ in range(num_rows)],
    'App_Name': [random.choice(['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Snapchat', 'WhatsApp']) for _ in range(num_rows)],
    'Screen_Time': np.random.randint(15, 300, size=num_rows),  # In minutes
    'Session_Count': np.random.randint(1, 20, size=num_rows),
    'Notifications_Received': np.random.randint(0, 50, size=num_rows),
    'Usage_Patterns': [random.choice(['Frequent', 'Occasional', 'Rare']) for _ in range(num_rows)],
    'Peak_Usage_Times': [random.choice(['Morning', 'Afternoon', 'Evening', 'Night']) for _ in range(num_rows)],
    'Break_Intervals': [random.choice(['Short', 'Medium', 'Long']) for _ in range(num_rows)]
}

# Function to introduce 25% errors
def introduce_errors(df, error_percentage=0.25):
    num_errors = int(df.shape[0] * error_percentage)  # Number of rows to introduce errors
    error_columns = df.columns.tolist()

    # Randomly introduce errors in the columns
    for column in error_columns:
        rows_with_errors = random.sample(range(df.shape[0]), num_errors)  # Random rows for errors
        for row in rows_with_errors:
            if column == 'Year':
                df.loc[row, column] = np.random.choice([9999, 2000])  # Invalid year
            elif column == 'Number_of_Enrollments':
                df.loc[row, column] = np.random.choice([99999, -1])  # Invalid enrollment count
            elif column == 'Dropout_Percentage':
                df.loc[row, column] = np.random.choice([999, -1])  # Invalid dropout percentage
            elif column == 'Literacy_Rate':
                df.loc[row, column] = np.random.choice([999, 'Invalid'])  # Invalid literacy rate
            elif column == 'Gender_Breakdown_Male':
                df.loc[row, column] = np.random.choice([9999, 'Invalid'])  # Invalid gender breakdown
            elif column == 'Infrastructure_Score':
                df.loc[row, column] = np.random.choice([999, 'Invalid'])  # Invalid infrastructure score
            elif column == 'Digital_Access':
                df.loc[row, column] = np.random.choice(['Invalid', 'Maybe'])  # Invalid digital access
            # Add more conditions for other columns if needed

    return df

# Create DataFrames
df_state_data = pd.DataFrame(state_data)
df_user_data = pd.DataFrame(user_data)

# Introduce errors in the data
df_state_data_with_errors = introduce_errors(df_state_data, error_percentage=0.25)
df_user_data_with_errors = introduce_errors(df_user_data, error_percentage=0.25)

# Create an Excel writer object and write the data to different sheets
with pd.ExcelWriter('Education_Enrollment_and_Social_Media_Usage_Data.xlsx') as writer:
    df_state_data_with_errors.to_excel(writer, sheet_name='State-wise Data', index=False)
    df_user_data_with_errors.to_excel(writer, sheet_name='User Data', index=False)

print("Data with 25% errors has been successfully generated and saved to 'Education_Enrollment_and_Social_Media_Usage_Data.xlsx'.")
