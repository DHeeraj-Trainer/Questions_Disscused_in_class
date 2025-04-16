# import pandas as pd
# import numpy as np
# import random
# from datetime import datetime, timedelta

# # Lists of Indian names and locations (more comprehensive lists can be found online)
# indian_first_names_male = ['Arjun', 'Aryan', 'Dev', 'Chaitanya', 'Sreeja', 'Teja', 'Madhusudhan', 'Raghavendra', 'Kranthi', 'Narayana', 'Srinivas', 'Sai', 'Anirudh', 'Prithvi', 'Brahma', 'Rajeshwar', 'Nikhil', 'Shiva', 'Vishnu', 'Yogesh', 'Manoj', 'Vamshi', 'Ravi', 'Mahesh', 'Nandu', 'Kiran', 'Sandeep', 'Venkatesh', 'Krishna', 'Ramakrishna', 'Narasimha', 'Venkat', 'Subrahmanyam', 'Raghav', 'Shankar', 'Harish', 'Teja', 'Arvind', 'Sushanth', 'Kalyan', 'Surya', 'Ganesh', 'Uday', 'Pradeep', 'Jagadish', 'Satish', 'Sandeep', 'Ravi Teja', 'Chaitanya', 'Vamsi', 'Lokesh', 'Srikar', 'Yashwanth', 'Babu', 'Vijay', 'Rajkumar', 'Sridhar', 'Mohan', 'Madhav', 'Ashwin', 'Rajeev', 'Sai Kumar', 'Kalyan', 'Shubham', 'Srinivasan', 'Akhil', 'Dinesh', 'Amit', 'Vishal', 'Karthik', 'Nithin', 'Vikram', 'Ravi Kumar', 'Anil Kumar', 'Jagan', 'Krishna Chaitanya', 'Rama Krishna', 'Raghavendra Prasad', 'Tejaswi','Karan', 'Rahul', 'Rohit', 'Prakash', 'Suresh', 'Vijay', 'Anil', 'Ramesh', 'Ganesh', 'Mahesh', 'Sunil', 'Rajesh','Aarav', 'Advait', 'Arjun', 'Aryan', 'Ashwin', 'Ayaan', 'Chirag', 'Dhruv', 'Gautam', 'Harsh', 'Ishan', 'Jai', 'Karan', 'Krishna', 'Lakshya', 'Manan', 'Nikhil', 'Om', 'Pranav', 'Raghav', 'Raj', 'Ravi', 'Reyansh', 'Rohit', 'Shaurya', 'Siddharth', 'Tanmay','Anirudh', 'Vamsikrishna', 'Harishankar', 'Kranthikumar', 'Aaditya', 'Vishvakarman', 'Jayanth', 'Samar', 'Tejendra', 'Bhaskar', 'Krishnamurthy', 'Chandramohan', 'Tejas', 'Suryanarayana', 'Sundar', 'Krishna Prasad', 'Bharadwaj', 'Nagendra', 'Suryakiran', 'Raghunandan', 'Siddharth', 'Akhilesh', 'Vishal Reddy', 'Ravi Shankar', 'Sandeep Kumar', 'Rajendra', 'Naveen', 'Anish', 'Ramachandra', 'Vinay', 'Sai Teja', 'Kalyana Sundaram', 'Balarama', 'Vikrant', 'Yogendra', 'Pranav Kumar', 'Pavan', 'Jagannatha', 'Sushil Kumar', 'Srinivasan', 'Sreeram', 'Madhavendra', 'Chandra', 'Ramesh', 'Srinivasa Reddy', 'Raghava Rao', 'Radhakrishna', 'Ravindra', 'Sai Ram', 'Narayana Rao', 'Sankaran', 'Gowtham', 'Bhanu', 'Jithendra', 'Sandeep Reddy', 'Chaitanya Kumar', 'Amit Reddy', 'Raghava', 'Siva Prasad', 'Bikram', 'Venkatraman', 'Vishwanath', 'Rajsekhar', 'Narayana', 'Chandrika', 'Aditya Kumar', 'Raghunath', 'Balaji', 'Vikas Reddy', 'Vajram', 'Venu Gopal', 'Abhinav', 'Satya', 'Aadhitya', 'Deva Prasad', 'Ravi Chandran','Ved', 'Vihaan', 'Vikas', 'Yash', 'Yogesh', 'Aadesh', 'Anil', 'Ankur', 'Bhavesh', 'Bharat', 'Chetan', 'Deepak', 'Gaurav', 'Harish', 'Hemant', 'Jatin', 'Kunal', 'Mahesh', 'Mayank', 'Nitin', 'Pankaj', 'Pradeep', 'Ramesh', 'Rajesh', 'Sameer', 'Sanjay', 'Santosh', 'Saurabh', 'Shankar', 'Sharad', 'Shyam', 'Sushil', 'Tarun', 'Uday', 'Umesh', 'Vikas', 'Vikram', 'Vishal', 'Vineet', 'Vinod', 'Yadav', 'Aditya', 'Akash', 'Alok', 'Avinash', 'Bhavin', 'Dev', 'Deepanshu', 'Farhan', 'Girish', 'Gokul', 'Hitesh', 'Indrajit', 'Jaiwant', 'Kiran', 'Krish', 'Mudit', 'Neeraj', 'Nishant', 'Parth', 'Rajeev', 'Rajendra', 'Rahul', 'Rohit', 'Ritesh', 'Shailesh', 'Shubham', 'Subhash', 'Suraj', 'Tanay', 'Tejas', 'Utkarsh', 'Varun', 'Vasant', 'Vijay', 'Vikrant', 'Vipul', 'Yuvraj',]
# indian_first_names_female = ['Priya', 'Deepika', 'Shweta', 'Neha', 'Pooja', 'Anjali', 'Rani', 'Seema', 'Kavita', 'Meena', 'Sangeeta', 'Rekha', 'Divya', 'Aarti', 'Jyoti','Aarti', 'Aishwarya', 'Akanksha', 'Ananya', 'Anjali', 'Aradhya', 'Bhuvana', 'Charulata', 'Chhavi', 'Divya', 'Durga', 'Gauri', 'Gayatri', 'Harini', 'Ishita', 'Jaya', 'Jyoti', 'Kavita', 'Khushboo', 'Komal', 'Kritika', 'Lakshmi', 'Manju', 'Meena', 'Neha','Anjali', 'Chandana', 'Sree Lakshmi', 'Savitri', 'Nitya', 'Srilakshmi', 'Kavya', 'Bhavana', 'Bhanupriya', 'Shalini', 'Nandini', 'Divya', 'Swapna', 'Vasundhara', 'Padmavathi', 'Kalyani', 'Aishwarya', 'Prathyusha', 'Sreeja', 'Madhavi', 'Anusha', 'Kavitha', 'Preeti', 'Lakshmi', 'Radhika', 'Shruti', 'Rashmi', 'Swathi', 'Suma', 'Poornima', 'Tejaswini', 'Priya', 'Srilakshmi', 'Saritha', 'Sindhu', 'Sonal', 'Rukmini', 'Uma', 'Gayatri', 'Sangeeta', 'Chaitanya', 'Pooja', 'Rithika', 'Sunitha', 'Yamini', 'Bhavani', 'Niharika', 'Ankitha', 'Shreya', 'Sangeetha', 'Priyanka', 'Rupa', 'Aparna', 'Kavitha', 'Lalitha', 'Sharanya', 'Vidhya', 'Manasa', 'Pavani', 'Sushma', 'Madhavi', 'Sridevi', 'Jaya', 'Madhuri', 'Renu', 'Lavanya', 'Shruthi', 'Srilakshmi', 'Simran', 'Nitya', 'Varshini', 'Rupali', 'Nanditha', 'Chaitanya', 'Rupal', 'Vasudha', 'Kalyani', 'Sridevi', 'Krithika', 'Swathi', 'Sravani', 'Chaitali', 'Meenakshi', 'Sharanya', 'Nidhi', 'Pooja', 'Priya', 'Radhika', 'Ritu', 'Roshni', 'Saanvi', 'Sakshi', 'Shalini', 'Shreya', 'Sneha', 'Swati', 'Tanvi', 'Trisha', 'Vidya', 'Yamini', 'Aditi', 'Amrita', 'Anuja', 'Arpita', 'Bhavna', 'Chitra', 'Damini', 'Deepika', 'Ekta', 'Geeta', 'Hemalata', 'Isha', 'Kiran', 'Kiranmayi', 'Laxmi', 'Mitali', 'Niharika', 'Pallavi', 'Poonam', 'Richa', 'Rupal', 'Shikha', 'Simran', 'Sonal', 'Sonia', 'Tanushree', 'Vidushi', 'Yashika', 'Akshita', 'Alisha', 'Anita', 'Ashima', 'Divyanshi', 'Gunjan', 'Harshita', 'Kanika', 'Kashish', 'Madhuri', 'Manisha', 'Mansi', 'Meenal', 'Mohini', 'Monika', 'Neelam', 'Nisha', 'Nutan', 'Pooja', 'Priyanka', 'Radhika', 'Rekha', 'Richa', 'Sagarika', 'Sakshi', 'Shreya', 'Shruti', 'Simran', 'Snehal', 'Sonal', 'Suman', 'Surbhi', 'Sweta', 'Tanvi', 'Tripti', 'Urvashi', 'Vaishali', 'Vasundhara', 'Vidhi', 'Vidhya', 'Zoya','Sridevi', 'Rani', 'Sindhura', 'Sukanya', 'Kiranmayi', 'Shravani', 'Priyanka Reddy', 'Sahithi', 'Sushmitha', 'Ananya Reddy', 'Charulatha', 'Indira', 'Vishala', 'Sowmya', 'Vamshi Priya', 'Padmavathi Reddy', 'Sahana', 'Srinidhi', 'Sumathi', 'Veena', 'Kavitha Reddy', 'Deepika', 'Shilpa', 'Nanditha Reddy', 'Yasmin', 'Aaradhya', 'Vaidehi', 'Srilekha', 'Nithya Reddy', 'Neelima', 'Madhavi Reddy', 'Ritika', 'Jeevitha', 'Kalyani Reddy', 'Tejasvi', 'Snehalata', 'Suma Reddy', 'Swarupa', 'Bharani', 'Aparna', 'Akhila', 'Mahitha', 'Keerthi', 'Sri Priya', 'Vennela', 'Vijaya', 'Sowmya Reddy', 'Vasundhara', 'Sumanthini', 'Amrutha', 'Anjali Reddy', 'Lavanya', 'Rashmika', 'Prashanti', 'Yamini Reddy', 'Sravya', 'Kavitha', 'Manju', 'Ravitha', 'Rupika', 'Neelaveni', 'Kriti', 'Supriya', 'Asha', 'Tejitha', 'Radhika Reddy', 'Pallavi', 'Chandana Reddy', 'Sreenidhi', 'Vaishnavi', 'Akhila Reddy', 'Sri Lakshmi', 'Keerthi Reddy', 'Madhuri', 'Lakshmi Reddy', 'Manasa', 'Sri Prathi', 'Simran Reddy', 'Anvi', 'Meenal', 'Gowri', 'Jeevanthi', 'Praneetha', 'Swetha', 'Nivedita', 'Charitha', 'Rupal', 'Sravani', 'Madhavi', 'Sushmitha Reddy', 'Bavitha', 'Mounika', 'Vidhya', 'Tanuja', 'Sreevani', 'Pooja Reddy', 'Anjali', 'Harini', 'Sreevathi', 'Sumathi', 'Bhavana Reddy', 'Sangita', 'Manisha', 'Sharanya']
# indian_last_names = ['Kumar', 'Singh', 'Patel', 'Sharma', 'Verma', 'Gupta', 'Joshi', 'Reddy', 'Naidu', 'Bhat', 'Das', 'Devi', 'Yadav', 'Khan', 'Choudhary']
# indian_cities_ap = ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Rajahmundry', 'Tirupati', 'Kakinada', 'Kadapa', 'Anantapur', 'Vizianagaram', 'Ongole', 'Eluru', 'Nandyal', 'Machilipatnam', 'Adoni', 'Tenali', 'Proddatur', 'Chittoor', 'Hindupur']
# indian_states = ['Andhra Pradesh', 'Telangana', 'Tamil Nadu', 'Karnataka', 'Maharashtra', 'Kerala', 'Uttar Pradesh', 'Madhya Pradesh', 'Gujarat', 'Rajasthan', 'Bihar', 'West Bengal', 'Odisha', 'Assam', 'Punjab', 'Haryana']
# indian_pin_codes_ap = [f'5{random.randint(0, 3)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}' for _ in range(len(indian_cities_ap))] # Example for AP

# def generate_indian_dirty_cloths_data(num_rows=10000):
#     """Generates a dirty sales dataset for a D Cloths store with Indian names and locations.

#     Args:
#         num_rows (int): The number of rows to generate in the dataset.

#     Returns:
#         pandas.DataFrame: A DataFrame containing the dirty sales data.
#     """

#     data = {
#         'OrderID': [random.randint(1000, 9999) for _ in range(num_rows)],
#         'CustomerID': [random.randint(1, 500) for _ in range(num_rows)],
#         'CustomerName': [f'{random.choice(indian_first_names_male + indian_first_names_female)} {random.choice(indian_last_names)}' for _ in range(num_rows)],
#         'Email': [f'customer{i}@email.com' for i in range(1, num_rows + 1)],
#         'PhoneNumber': [f'{random.choice([6, 7, 8, 9])}{"".join(random.choices("0123456789", k=9))}' for _ in range(num_rows)],
#         'OrderDate': [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(num_rows)],
#         'ProductCategory': random.choices(['Tops', 'Bottoms', 'Dresses', 'Outerwear', 'Accessories'], k=num_rows),
#         'ProductName': [f'{random.choice(["Cotton", "Linen", "Silk", "Wool"])} {random.choice(["Kurti", "Salwar", "Saree", "Shawl", "Top", "Shirt", "Pant", "Lehenga"])}' for _ in range(num_rows)],
#         'Quantity': [random.randint(1, 5) for _ in range(num_rows)],
#         'UnitPrice': [round(random.uniform(100, 5000), 2) for _ in range(num_rows)], # Prices in INR
#         'DiscountPercentage': [round(random.uniform(0, 0.5), 2) for _ in range(num_rows)],
#         'ShippingAddress': [f'{random.randint(10, 500)}, {random.choice(["Main Road", "Cross Street", "Gandhi Nagar"])}' for _ in range(num_rows)],
#         'ShippingCity': random.choices(indian_cities_ap, k=num_rows),
#         'ShippingState': ['Andhra Pradesh'] * num_rows,
#         'ShippingPincode': [random.choice(indian_pin_codes_ap) for _ in range(num_rows)],
#         'BillingAddress': [f'{random.randint(10, 500)}, {random.choice(["MG Road", "Nehru Street", "Indira Colony"])}' for _ in range(num_rows)],
#         'BillingCity': random.choices(indian_cities_ap, k=num_rows),
#         'BillingState': ['Andhra Pradesh'] * num_rows,
#         'BillingPincode': [random.choice(indian_pin_codes_ap) for _ in range(num_rows)],
#         'PaymentMethod': random.choices(['Credit Card', 'Debit Card', 'Cash on Delivery', 'UPI', 'Net Banking'], k=num_rows),
#         'ShippingCarrier': random.choices(['India Post', 'Blue Dart', 'Delhivery', 'Ekart', 'Local Delivery', None], weights=[0.3, 0.2, 0.2, 0.1, 0.1, 0.1], k=num_rows),
#         'TrackingNumber': [f'TRACK{random.randint(10000000, 99999999)}' if random.random() > 0.15 else None for _ in range(num_rows)],
#         'OrderStatus': random.choices(['Processing', 'Shipped', 'Delivered', 'Cancelled', 'Returned'], k=num_rows),
#         'SalesPerson': [f'Salesperson {random.randint(1, 15)}' for _ in range(num_rows)],
#         'Region': random.choices(['South', 'East', 'West', 'North', 'Central'], k=num_rows),
#         'Country': ['India'] * num_rows,
#         'GST_Number': [f'{random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}{random.randint(10, 99)}{random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}{random.randint(1000, 9999)}{random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}{1}{random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}' if random.random() > 0.3 else None for _ in range(num_rows)],
#         'ReturnReason': [random.choice(['Size Issue', 'Color Mismatch', 'Defective Product', 'Not as Described', None]) if random.random() < 0.08 else None for _ in range(num_rows)],
#         'ReviewRating': [random.randint(1, 5) if random.random() < 0.4 else None for _ in range(num_rows)],
#         'Notes': [f'Urgent delivery for order {i}' if random.random() < 0.05 else None for i in range(num_rows)],
#         'LastModified': [datetime.now() - timedelta(hours=random.randint(0, 48)) for _ in range(num_rows)]
#     }

#     df = pd.DataFrame(data)

#     # Introduce Null Values
#     for col in df.columns:
#         if df[col].dtype == 'object' or col in ['DiscountPercentage', 'ReviewRating', 'TrackingNumber', 'GST_Number', 'ReturnReason', 'Notes', 'ShippingCarrier']:
#             mask = np.random.choice([True, False], size=len(df), p=[0.15, 0.85]) # Increased chance of NaN for some columns
#             df.loc[mask, col] = np.nan
#         elif df[col].dtype in ['int64', 'float64']:
#             mask = np.random.choice([True, False], size=len(df), p=[0.08, 0.92])
#             df.loc[mask, col] = np.nan
#         elif df[col].dtype == '<M8[ns]':
#             mask = np.random.choice([True, False], size=len(df), p=[0.05, 0.95])
#             df.loc[mask, col] = pd.NaT

#     # Introduce Duplicate Rows
#     num_duplicates = int(0.08 * num_rows) # Increased percentage of duplicates
#     duplicate_indices = random.sample(range(num_rows), num_duplicates)
#     df = pd.concat([df, df.iloc[duplicate_indices]], ignore_index=True)
#     df = df.sample(frac=1).reset_index(drop=True)

#     # Introduce Outliers
#     # Quantity outliers
#     q_high_outlier_indices = random.sample(df.index.tolist(), int(0.02 * num_rows))
#     df.loc[q_high_outlier_indices, 'Quantity'] = [random.randint(15, 30) for _ in range(len(q_high_outlier_indices))]
#     q_low_outlier_indices = random.sample(df.index.tolist(), int(0.01 * num_rows))
#     df.loc[q_low_outlier_indices, 'Quantity'] = 0

#     # UnitPrice outliers (adjusting ranges for INR)
#     p_high_outlier_indices = random.sample(df.index.tolist(), int(0.02 * num_rows))
#     df.loc[p_high_outlier_indices, 'UnitPrice'] = [round(random.uniform(8000, 20000), 2) for _ in range(len(p_high_outlier_indices))]
#     p_low_outlier_indices = random.sample(df.index.tolist(), int(0.01 * num_rows))
#     df.loc[p_low_outlier_indices, 'UnitPrice'] = [round(random.uniform(10, 50), 2) for _ in range(len(p_low_outlier_indices))]

#     # Introduce Inconsistent Data
#     # Inconsistent Order Status for older dates
#     old_date_mask = df['OrderDate'] < datetime.now() - timedelta(days=400)
#     df.loc[old_date_mask, 'OrderStatus'] = df.loc[old_date_mask, 'OrderStatus'].apply(lambda x: random.choice(['Delivered', 'Cancelled']) if pd.notna(x) else x)

#     # Inconsistent Discount with Price
#     high_price_no_discount_mask = (df['UnitPrice'] > 4000) & (df['DiscountPercentage'] == 0) & (np.random.rand(len(df)) < 0.1)
#     df.loc[high_price_no_discount_mask, 'DiscountPercentage'] = round(random.uniform(0.1, 0.3), 2)

#     # Introduce Typos/Inconsistent Formatting (expanded for Indian context)
#     typo_indices = random.sample(df.index.tolist(), int(0.03 * num_rows))
#     for index in typo_indices:
#         if isinstance(df.loc[index, 'ProductName'], str) and len(df.loc[index, 'ProductName']) > 4:
#             pos = random.randint(0, len(df.loc[index, 'ProductName']) - 1)
#             original_char = df.loc[index, 'ProductName'][pos]
#             if original_char.isalpha():
#                 new_char = random.choice([c for c in "abcdefghijklmnopqrstuvwxyz" if c != original_char.lower() and c != original_char.upper()])
#                 df.loc[index, 'ProductName'] = df.loc[index, 'ProductName'][:pos] + new_char + df.loc[index, 'ProductName'][pos+1:]
#         if isinstance(df.loc[index, 'PaymentMethod'], str):
#             if df.loc[index, 'PaymentMethod'] == 'Cash on Delivery':
#                 df.loc[index, 'PaymentMethod'] = random.choice(['COD', 'Cash on delivery', 'Cash  on Delivery'])
#             elif df.loc[index, 'PaymentMethod'] == 'UPI':
#                 df.loc[index, 'PaymentMethod'] = random.choice(['upi', '*UPI*', 'U P I'])
#         if isinstance(df.loc[index, 'ShippingCity'], str) and len(df.loc[index, 'ShippingCity']) > 3:
#             if random.random() < 0.2:
#                 pos = random.randint(0, len(df.loc[index, 'ShippingCity']) - 1)
#                 original_char = df.loc[index, 'ShippingCity'][pos]
#                 if original_char.isalpha():
#                     new_char = random.choice([c for c in "abcdefghijklmnopqrstuvwxyz" if c != original_char.lower() and c != original_char.upper()])
#                     df.loc[index, 'ShippingCity'] = df.loc[index, 'ShippingCity'][:pos] + new_char + df.loc[index, 'ShippingCity'][pos+1:]

#     return df

# if __name__ == "__main__":
#     dirty_data_indian = generate_indian_dirty_cloths_data(num_rows=1000)
#     print(dirty_data_indian.head())
#     print(dirty_data_indian.info())

#     # Save to a CSV file
#     dirty_data_indian.to_csv('dirty_indian_cloths_sales_data.csv', index=False)
#     print("\nDirty Indian dataset saved to dirty_indian_cloths_sales_data.csv")


import pandas as pd
import random
from faker import Faker
from datetime import timedelta
import uuid

fake = Faker('en_IN')
num_rows = 10000

def random_choice(choices):
    return random.choice(choices)

def generate_data(n):
    data = []
    for _ in range(n):
        customer_id = str(uuid.uuid4())[:8]
        order_id = str(uuid.uuid4())[:10]
        product_id = f"P{random.randint(1000, 9999)}"
        store_id = f"S{random.randint(1, 10)}"
        name = fake.name()
        age = random.randint(18, 65)
        gender = random_choice(["Male", "Female", "Other"])
        phone = fake.phone_number()
        email = fake.email()
        city = fake.city()
        state = fake.state()
        pincode = fake.postcode()
        address = fake.address()

        product_name = random_choice([
    "Kurta", "Saree", "Sherwani", "Lehenga", "Blouse", "Dupatta", "Churidar", "Anarkali", "Salwar", "Kameez",
    "Palazzo", "Tunic", "Kaftan", "Jumpsuit", "Pants", "Skirt", "Maxi Dress", "A-line Dress", "Petticoat", "Dhoti",
    "Tunics", "Peplum Top", "Flared Pants", "Jeggings", "Culottes", "Suits", "Tops", "T-Shirts", "Shirts",
    "Denim Jacket", "Leather Jacket", "Blazer", "Vest", "Choli", "Crop Top", "Kaftan Dress", "Robe", "Wrap Dress", "Kimono",
    "Shawl", "Poncho", "Sweater", "Cardigan", "Coat", "Parka", "Raincoat", "Tweed Coat", "Overcoat", "Bomber Jacket", "Trench Coat",
    "Kimono Robe", "Capes", "Sari Gown", "Midi Dress", "Shirt Dress"
])
        brand = random_choice([
    "FabIndia", "Biba", "Manyavar", "W", "Utsa", "Soch", "H&M", "Zara", "Myntra", "Ajio", "Max", "Van Heusen", "Levi's", "Raymond",
    "Pantaloons", "Shoppers Stop", "Lifestyle", "Aurelia", "Allen Solly", "Marks & Spencer", "Peter England",
    "Lacoste", "Tommy Hilfiger", "Calvin Klein", "Forever 21", "Puma", "Adidas", "Reebok", "Nike", "Under Armour", "Pepe Jeans"
])
        color = random_choice([
    "Red", "Blue", "Green", "Yellow", "Black", "White", "Maroon", "Pink", "Purple", "Orange", "Brown", "Gray", "Beige", "Turquoise",
    "Lavender", "Magenta", "Sky Blue", "Navy Blue", "Emerald Green", "Olive"
])
        material = random_choice([
    "Cotton", "Silk", "Linen", "Rayon", "Georgette", "Chiffon", "Satin", "Velvet", "Denim", "Fleece", "Leather", "Suede", "Jersey",
    "Wool", "Knit", "Taffeta", "Cashmere", "Corduroy", "Crepe", "Tulle", "Canvas", "Brocade", "Organza", "Poplin", "Jute", "Spandex",
    "Tencel", "Viscose", "Polyester", "Nylon", "Acrylic", "Bamboo", "Microfiber", "Lace", "Sequin", "Suede Leather", "Chambray",
    "Georgette Silk", "Polycrepe", "Faux Leather", "Faux Fur"
])


        category = random_choice(["Men", "Women", "Kids"])
        brand = random_choice(["FabIndia", "Biba", "Manyavar", "W", "Utsa", "Soch"])
        size = random_choice(["XS", "S", "M", "L", "XL", "XXL"])
        color = random_choice(["Red", "Blue", "Green", "Yellow", "Black", "White", "Maroon"])
        material = random_choice(["Cotton", "Silk", "Linen", "Rayon", "Georgette", "Chiffon"])

        order_date = fake.date_between(start_date='-1y', end_date='today')
        quantity = random.randint(1, 5)
        price_per_unit = round(random.uniform(500, 5000), 2)
        discount = round(random.uniform(0, 0.3), 2)
        total_price = round(quantity * price_per_unit * (1 - discount), 2)
        payment_method = random_choice(["Credit Card", "Debit Card", "UPI", "Cash on Delivery", "Net Banking"])
        transaction_id = str(uuid.uuid4())[:12]
        gst_applied = round(total_price * 0.05, 2)

        shipping_provider = random_choice(["Delhivery", "BlueDart", "India Post", "Ecom Express", "Shadowfax"])
        shipping_cost = round(random.uniform(30, 150), 2)
        delivery_status = random_choice(["Delivered", "In Transit", "Pending", "Cancelled"])
        estimated_delivery = order_date + timedelta(days=random.randint(3, 7))
        actual_delivery = estimated_delivery + timedelta(days=random.choice([0, 1, -1, 2, -2]))

        store_city = fake.city()
        store_state = fake.state()
        return_status = random_choice(["Returned", "Not Returned"])
        review_rating = round(random.uniform(1, 5), 1)
        customer_loyalty = random_choice(["Bronze", "Silver", "Gold", "Platinum"])
        referred_by = fake.name() if random.random() < 0.1 else None

        row = {
            "Customer_ID": customer_id,
            "Order_ID": order_id,
            "Product_ID": product_id,
            "Store_ID": store_id,
            "Customer_Name": name,
            "Age": age,
            "Gender": gender,
            "Phone": phone,
            "Email": email,
            "City": city,
            "State": state,
            "Pincode": pincode,
            "Address": address,
            "Product_Name": product_name,
            "Category": category,
            "Brand": brand,
            "Size": size,
            "Color": color,
            "Material": material,
            "Order_Date": order_date,
            "Quantity": quantity,
            "Price_Per_Unit": price_per_unit,
            "Discount": discount,
            "Total_Price": total_price,
            "GST": gst_applied,
            "Payment_Method": payment_method,
            "Transaction_ID": transaction_id,
            "Shipping_Provider": shipping_provider,
            "Shipping_Cost": shipping_cost,
            "Delivery_Status": delivery_status,
            "Estimated_Delivery": estimated_delivery,
            "Actual_Delivery": actual_delivery,
            "Store_City": store_city,
            "Store_State": store_state,
            "Return_Status": return_status,
            "Review_Rating": review_rating,
            "Customer_Loyalty": customer_loyalty,
            "Referred_By": referred_by
        }

        data.append(row)
    return pd.DataFrame(data)

df = generate_data(num_rows)

# Save to CSV
df.to_csv("synthetic_indian_clothing_store_data.csv", index=False)
print("✅ Dataset generated and saved as 'synthetic_indian_clothing_store_data.csv'")
