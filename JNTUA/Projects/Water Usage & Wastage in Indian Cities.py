import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize the Faker instance
fake = Faker()

# List of Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Surat", 
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Madurai", "Faridabad", "Rajkot", "Kochi", "Coimbatore", "Noida", "Chandigarh", "Guwahati", 
    "Mysuru", "Vijayawada", "Agra", "Jabalpur"
]

# Function to generate a random date within a range
def random_date(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date
    random_day = np.random.randint(0, delta.days)
    return start_date + timedelta(days=random_day)

# Simulate Consumption Data for 3 years
def generate_consumption_data(n, start_date, end_date):
    data = []
    for _ in range(n):
        household_id = fake.uuid4()
        timestamp = random_date(start_date, end_date)
        water_usage = np.random.randint(50, 300)  # Random water usage between 50L and 300L
        water_source = np.random.choice(['Municipal', 'Borewell', 'Tanker'])
        usage_type = np.random.choice(['Drinking', 'Cooking', 'Cleaning', 'Gardening'])
        consumption_zone = np.random.choice(indian_cities)  # Random Indian city
        water_meter_type = np.random.choice(['Smart Meter', 'Manual Meter'])
        water_tariff = np.random.randint(10, 30)  # Cost of water per liter
        avg_household_size = np.random.randint(1, 6)  # Household size between 1 and 5
        day_of_week = timestamp.strftime('%A')
        holiday_indicator = np.random.choice([0, 1])  # Random holiday indicator
        water_usage_per_capita = water_usage / avg_household_size
        peak_usage_hour = np.random.choice(['Morning', 'Afternoon', 'Evening'])
        usage_category = np.random.choice(['High', 'Medium', 'Low'])
        
        data.append([household_id, timestamp, water_usage, water_source, usage_type, consumption_zone, 
                     water_meter_type, water_tariff, avg_household_size, day_of_week, holiday_indicator, 
                     water_usage_per_capita, peak_usage_hour, usage_category])
    
    return data

# Simulate Infrastructure Data
def generate_infrastructure_data(n):
    data = []
    for _ in range(n):
        pipe_network_id = fake.uuid4()
        pipe_material = np.random.choice(['PVC', 'Steel', 'Cast Iron'])
        pipe_diameter = np.random.randint(100, 500)  # Pipe diameter in mm
        pipe_length = np.random.randint(5, 50)  # Pipe length in km
        pipe_condition = np.random.choice(['New', 'Good', 'Damaged', 'Leaking'])
        maintenance_date = random_date('2019-01-01', '2021-12-31')
        next_maintenance_date = random_date('2021-01-01', '2023-12-31')
        pipe_age = np.random.randint(5, 50)  # Pipe age in years
        maintenance_duration = np.random.randint(2, 10)  # Duration in hours
        service_interruptions = np.random.randint(0, 3)  # Number of interruptions
        repair_cost = np.random.randint(5000, 50000)  # Repair cost in INR
        water_quality = np.random.choice(['Safe', 'Contaminated', 'Potable'])
        
        data.append([pipe_network_id, pipe_material, pipe_diameter, pipe_length, pipe_condition, 
                     maintenance_date, next_maintenance_date, pipe_age, maintenance_duration, 
                     service_interruptions, repair_cost, water_quality])
    
    return data

# Simulate Environmental Data
def generate_environmental_data(n, start_date, end_date):
    data = []
    for _ in range(n):
        timestamp = random_date(start_date, end_date)
        rainfall = np.random.uniform(0, 100)  # Rainfall in mm
        temperature = np.random.uniform(20, 40)  # Temperature in Celsius
        humidity = np.random.uniform(30, 90)  # Humidity in percentage
        aqi = np.random.randint(50, 300)  # Air Quality Index
        wind_speed = np.random.uniform(5, 20)  # Wind speed in km/h
        evaporation_rate = np.random.uniform(1, 10)  # Evaporation rate in mm
        soil_moisture = np.random.uniform(10, 60)  # Soil moisture percentage
        water_table_level = np.random.uniform(10, 500)  # Depth of water table in meters
        season = np.random.choice(['Summer', 'Monsoon', 'Winter'])
        flooding_indicator = np.random.choice([0, 1])  # Whether there was flooding
        rainwater_harvesting_activity = np.random.choice([0, 1])  # Activity indicator
        
        data.append([timestamp, rainfall, temperature, humidity, aqi, wind_speed, evaporation_rate, 
                     soil_moisture, water_table_level, season, flooding_indicator, rainwater_harvesting_activity])
    
    return data

# Simulate Leakage Reports
def generate_leakage_reports(n, start_date, end_date):
    data = []
    for _ in range(n):
        leak_location = np.random.choice(indian_cities)
        detection_time = random_date(start_date, end_date)
        leak_volume = np.random.uniform(50, 2000)  # Leak volume in liters
        leak_type = np.random.choice(['Minor', 'Major', 'Burst'])
        leak_severity = np.random.choice(['Low', 'Medium', 'High'])
        leak_duration = np.random.randint(2, 48)  # Leak duration in hours
        cause_of_leak = np.random.choice(['Corrosion', 'Physical Damage', 'Ageing'])
        repair_status = np.random.choice([0, 1])  # Whether repaired or not
        repair_time = np.random.randint(2, 24)  # Repair time in hours
        detection_method = np.random.choice(['Smart Metering', 'Manual Inspection'])
        report_by = fake.name()
        leak_response_time = np.random.randint(1, 10)  # Time taken to respond to the leak in hours
        
        data.append([leak_location, detection_time, leak_volume, leak_type, leak_severity, leak_duration, 
                     cause_of_leak, repair_status, repair_time, detection_method, report_by, leak_response_time])
    
    return data

# Generating data
num_consumption_data = 10000
num_infrastructure_data = 50
num_environmental_data = 365 * 3  # For 3 years of daily data
num_leakage_reports = 500

# Define time range for data generation
start_date = '2019-01-01'
end_date = '2022-12-31'

# Generate Data
consumption_data = generate_consumption_data(num_consumption_data, start_date, end_date)
infrastructure_data = generate_infrastructure_data(num_infrastructure_data)
environmental_data = generate_environmental_data(num_environmental_data, start_date, end_date)
leakage_reports = generate_leakage_reports(num_leakage_reports, start_date, end_date)

# Create DataFrames
consumption_df = pd.DataFrame(consumption_data, columns=['Household ID', 'Timestamp', 'Water Usage (Liters)', 'Water Source', 'Usage Type', 'Consumption Zone', 
                                                         'Water Meter Type', 'Water Tariff', 'Avg Household Size', 'Day of Week', 'Holiday Indicator', 
                                                         'Water Usage (Per Capita)', 'Peak Usage Hour', 'Water Usage Category'])

infrastructure_df = pd.DataFrame(infrastructure_data, columns=['Pipe Network ID', 'Pipe Material', 'Pipe Diameter', 'Pipe Length', 'Pipe Condition', 
                                                              'Maintenance Date', 'Next Scheduled Maintenance', 'Pipe Age', 'Maintenance Duration', 
                                                              'Service Interruptions', 'Repair Cost', 'Water Quality'])

environmental_df = pd.DataFrame(environmental_data, columns=['Timestamp', 'Rainfall (mm)', 'Temperature (°C)', 'Humidity (%)', 'Air Quality Index (AQI)', 
                                                             'Wind Speed (km/h)', 'Evaporation Rate (mm)', 'Soil Moisture (%)', 'Water Table Level (m)', 
                                                             'Season', 'Flooding Indicator', 'Rainwater Harvesting Activity'])

leakage_df = pd.DataFrame(leakage_reports, columns=['Leak Location', 'Detection Time', 'Leak Volume (Liters)', 'Leak Type', 'Leak Severity', 'Leak Duration (hrs)', 
                                                   'Cause of Leak', 'Repair Status', 'Repair Time (hrs)', 'Leak Detection Method', 'Leak Reported By', 'Leak Response Time (hrs)'])

# Introduce 20% error rate (randomly replace some values with NaN or incorrect values)
def introduce_errors(df, error_rate=0.2):
    for col in df.columns:
        num_errors = int(len(df) * error_rate)
        error_indices = np.random.choice(df.index, size=num_errors, replace=False)
        for idx in error_indices:
            if np.random.rand() < 0.5:
                df.loc[idx, col] = np.nan  # Set to NaN (missing value)
            else:
                df.loc[idx, col] = "ERROR"  # Introduce incorrect value
    return df

# Apply errors to the dataframes
consumption_df = introduce_errors(consumption_df)
infrastructure_df = introduce_errors(infrastructure_df)
environmental_df = introduce_errors(environmental_df)
leakage_df = introduce_errors(leakage_df)

# Write data to Excel
with pd.ExcelWriter('water_usage_wastage_indian_cities.xlsx') as writer:
    consumption_df.to_excel(writer, sheet_name='Consumption Data', index=False)
    infrastructure_df.to_excel(writer, sheet_name='Infrastructure Data', index=False)
    environmental_df.to_excel(writer, sheet_name='Environmental Data', index=False)
    leakage_df.to_excel(writer, sheet_name='Leakage Reports', index=False)

print("Water Usage, Infrastructure, Environmental Data, and Leakage Reports created and saved successfully!")
