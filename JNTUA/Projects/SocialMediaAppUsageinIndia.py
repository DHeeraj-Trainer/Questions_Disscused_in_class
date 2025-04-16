import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize the Faker object
fake = Faker()

# Define lists for generating random data
genders = ['Male', 'Female', 'Other']
occupations = ['Student', 'Professional', 'Retired', 'Unemployed']
marital_status = ['Single', 'Married', 'Widowed']
education_levels = ['High School', 'Undergraduate', 'Postgraduate']
income_levels = ['Low', 'Middle', 'High']
device_types = ['Android', 'iOS', 'Tablet']
app_sources = ['Google Play', 'Apple Store', 'Other']
regions = ['North', 'South', 'East', 'West']
apps = ['Instagram', 'WhatsApp', 'Facebook', 'TikTok', 'Twitter']
usage_patterns = ['Binge', 'Regular', 'Rare']
peak_times = ['Morning', 'Afternoon', 'Evening', 'Night']
break_intervals = ['5 mins every hour', '10 mins every hour', 'None']
frequency = ['Daily', 'Weekly', 'Monthly']
content_types = ['Videos', 'Photos', 'Text Posts', 'Stories']
purposes = ['Socializing', 'Entertainment', 'Work', 'News', 'Education']

# Generate columns
num_rows = 10000
data = {
    'User_ID': [f'U{str(i).zfill(4)}' for i in range(1, num_rows + 1)],
    'Age': np.random.randint(18, 60, size=num_rows),
    'Gender': np.random.choice(genders, size=num_rows),
    'Location': [fake.city() for _ in range(num_rows)],
    'Occupation': np.random.choice(occupations, size=num_rows),
    'Marital_Status': np.random.choice(marital_status, size=num_rows),
    'Education_Level': np.random.choice(education_levels, size=num_rows),
    'Income_Level': np.random.choice(income_levels, size=num_rows),
    'Device_Type': np.random.choice(device_types, size=num_rows),
    'App_Download_Source': np.random.choice(app_sources, size=num_rows),
    'Region': np.random.choice(regions, size=num_rows),
    'App_Name': np.random.choice(apps, size=num_rows),
    'Screen_Time': np.random.randint(30, 300, size=num_rows),  # in minutes
    'Session_Count': np.random.randint(1, 20, size=num_rows),
    'Notifications_Received': np.random.randint(0, 50, size=num_rows),
    'Time_Spent_Per_Session': np.random.randint(5, 30, size=num_rows),  # in minutes
    'App_Installs': np.random.choice(['Yes', 'No'], size=num_rows),
    'App_Version': np.random.choice(['v1.0', 'v1.1', 'v1.2', 'Latest', 'Beta'], size=num_rows),
    'Usage_Patterns': np.random.choice(usage_patterns, size=num_rows),
    'Peak_Usage_Times': np.random.choice(peak_times, size=num_rows),
    'Break_Intervals': np.random.choice(break_intervals, size=num_rows),
    'Usage_Frequency': np.random.choice(frequency, size=num_rows),
    'App_Addiction_Level': np.random.randint(0, 101, size=num_rows),  # 0 to 100 scale
    'Engagement_Level': np.random.randint(0, 101, size=num_rows),  # 0 to 100 scale
    'Social_Interaction': np.random.randint(0, 500, size=num_rows),
    'App_Purpose': np.random.choice(purposes, size=num_rows),
    'Content_Type': np.random.choice(content_types, size=num_rows),
    'Average_Interaction_Time': np.random.randint(5, 30, size=num_rows),  # in minutes
    'Sleep_Disruption': np.random.randint(0, 11, size=num_rows),  # 0 to 10 scale
    'Distraction_Level': np.random.randint(1, 11, size=num_rows),  # 1 to 10 scale
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Introduce 25% errors in the data
error_columns = ['Age', 'Gender', 'Screen_Time', 'Session_Count', 'App_Installs', 'App_Addiction_Level']

# Function to introduce errors
def introduce_errors(df, error_columns, error_percentage=0.25):
    num_errors = int(df.shape[0] * error_percentage)  # Number of rows to introduce errors
    for column in error_columns:
        rows_with_errors = random.sample(range(df.shape[0]), num_errors)  # Random rows
        for row in rows_with_errors:
            if column == 'Age':
                df.loc[row, column] = np.random.choice([99, -1, 'Invalid'])  # Invalid age value
            elif column == 'Gender':
                df.loc[row, column] = np.random.choice(['Invalid', 'Other', 'Male', 'Female', 'Unknown'])
            elif column == 'Screen_Time':
                df.loc[row, column] = np.random.choice([9999, 'Invalid'])  # Invalid screen time
            elif column == 'Session_Count':
                df.loc[row, column] = np.random.choice([9999, 'Invalid'])
            elif column == 'App_Installs':
                df.loc[row, column] = np.random.choice(['Invalid', 'No', 'Yes'])
            elif column == 'App_Addiction_Level':
                df.loc[row, column] = np.random.choice([9999, 'Invalid'])

    return df

# Introduce errors in the dataset
df_with_errors = introduce_errors(df, error_columns, error_percentage=0.25)

# Save the generated data to a CSV file
df_with_errors.to_csv('Social_Media_App_Usage_India.csv', index=False)

print("Data with errors has been successfully generated and saved to 'Social_Media_App_Usage_India.csv'")
