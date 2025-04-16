import pandas as pd
import random
from faker import Faker
import numpy as np
from datetime import datetime, timedelta

# Initialize Faker for realistic data
fake = Faker()

# Set the seed for reproducibility
random.seed(42)
np.random.seed(42)

# Constants for Store, Product Details, and Sales Data
NUM_ROWS = 10000
NUM_STORES = 50
NUM_PRODUCTS = 50
CITIES = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
PRODUCT_CATEGORIES = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys', 'Sports']
PRODUCT_TYPES = ['Physical', 'Digital', 'Service']
SALES_CHANNELS = ['Online', 'In-Store', 'Mobile App']
SEASONALITY = ['Winter', 'Spring', 'Summer', 'Fall']
PURCHASE_METHODS = ['Online', 'In-Store', 'App']
SATISFACTION_SCORE = [1, 2, 3, 4, 5]
WEATHER_CONDITIONS = ['Sunny', 'Rainy', 'Snowy', 'Cloudy', 'Windy']
LOCAL_EVENTS = ['Football Game', 'Concert', 'Festival', 'None']
ECONOMIC_CONDITIONS = ['Boom', 'Recession', 'Stable']
PROMOTIONS = ['Discount', 'Buy 1 Get 1 Free', 'None']
SOCIAL_MEDIA_SENTIMENT = ['Positive', 'Neutral', 'Negative']
COMPETITOR_PROMOTIONS = ['Discount', 'Buy 1 Get 1 Free', 'None']
STAGES = ['Introduction', 'Growth', 'Maturity', 'Decline']

# Helper function to generate random dates within the last 3 years
def random_date(start_date, end_date):
    return fake.date_between(start_date=start_date, end_date=end_date)

# Helper function to generate random product prices
def random_price():
    return round(random.uniform(5, 500), 2)

# Helper function to generate random product stock levels
def random_stock_level():
    return random.randint(10, 200)

# Create the Store Details Data
store_data = []
for store_id in range(1, NUM_STORES + 1):
    store_name = fake.company()
    store_location = random.choice(CITIES)
    store_type = random.choice(['Flagship', 'Outlet', 'Pop-up'])
    store_size = random.choice(['Small', 'Medium', 'Large'])
    store_manager = fake.name()
    
    store_data.append([
        f"Store_{store_id}", store_name, store_location, store_type, store_size, store_manager
    ])

# Create the Product Details Data
product_data = []
for product_id in range(1, NUM_PRODUCTS + 1):
    product_name = f"Product_{product_id}"
    category = random.choice(PRODUCT_CATEGORIES)
    price = random_price()
    product_type = random.choice(PRODUCT_TYPES)
    brand = fake.company()
    description = fake.text(max_nb_chars=200)
    stock_level = random_stock_level()
    supplier_id = fake.uuid4()
    
    product_data.append([
        f"Product_{product_id}", product_name, category, price, product_type, brand, description, stock_level, supplier_id
    ])

# Create the Sales Data
data = []
start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 1, 1)

for i in range(NUM_ROWS):
    # Sales Data
    store_id = f"Store_{random.randint(1, NUM_STORES)}"
    product_id = f"Product_{random.randint(1, NUM_PRODUCTS)}"
    date = random_date(start_date, end_date)
    units_sold = random.randint(1, 100)
    price = random_price()
    revenue = units_sold * price
    discount = random.choice([0, random.uniform(0.05, 0.3)])  # No discount or 5% - 30% discount
    sales_channel = random.choice(SALES_CHANNELS)
    store_location = random.choice(CITIES)
    store_type = random.choice(['Flagship', 'Outlet', 'Pop-up'])
    time_of_sale = random.choice(['Morning', 'Afternoon', 'Evening'])
    seasonality_indicator = random.choice(SEASONALITY)
    stock_availability = random.choice(['Yes', 'No'])
    sales_representative = fake.name()

    # Customer Data
    customer_id = fake.uuid4()
    age = random.randint(18, 70)
    gender = random.choice(['Male', 'Female'])
    income_level = random.choice(['Low', 'Middle', 'High'])
    loyalty_program_status = random.choice(['Yes', 'No'])
    clv = random.randint(100, 5000)
    purchase_frequency = random.choice(['Weekly', 'Monthly', 'Annually'])
    avg_basket_size = random.randint(1, 10)
    purchase_method = random.choice(PURCHASE_METHODS)
    first_purchase_date = random_date(start_date, date)
    last_purchase_date = random_date(first_purchase_date, date)
    satisfaction_score = random.choice(SATISFACTION_SCORE)

    # Product Data
    product_name = f"Product_{random.randint(1, 100)}"
    category = random.choice(PRODUCT_CATEGORIES)
    product_price = random_price()
    brand = fake.company()
    product_type = random.choice(PRODUCT_TYPES)
    product_size = random.choice(['Small', 'Medium', 'Large'])
    product_color = random.choice(['Red', 'Blue', 'Green', 'Black', 'White'])
    product_rating = round(random.uniform(1, 5), 1)
    stock_level = random_stock_level()
    restock_date = random_date(datetime(2023, 1, 1), end_date)
    supplier_id = fake.uuid4()
    product_lifecycle_stage = random.choice(STAGES)
    product_description = fake.text(max_nb_chars=200)
    shipping_weight = round(random.uniform(0.1, 10), 2)  # In kg
    return_rate = round(random.uniform(0, 0.3), 2)

    # External Factors
    promotions = random.choice(PROMOTIONS)
    holidays = random.choice(['Christmas', 'Black Friday', 'None'])
    competitor_pricing = round(random.uniform(5, 500), 2)
    competitor_promotions = random.choice(COMPETITOR_PROMOTIONS)
    market_trend = random.choice(['Yes', 'No'])
    weather = random.choice(WEATHER_CONDITIONS)
    local_events = random.choice(LOCAL_EVENTS)
    economic_conditions = random.choice(ECONOMIC_CONDITIONS)
    advertising_spend = round(random.uniform(1000, 10000), 2)
    social_media_sentiment = random.choice(SOCIAL_MEDIA_SENTIMENT)
    competitor_product_launch = random.choice(['Yes', 'No'])
    pricing_changes = random.choice(['Increased', 'Decreased', 'Stable'])
    shipping_promotions = random.choice(['Free Shipping', 'Expedited Shipping', 'None'])

    # Append the row to data
    data.append([
        store_id, product_id, date, units_sold, revenue, discount, sales_channel, store_location, 
        store_type, time_of_sale, seasonality_indicator, stock_availability, sales_representative,
        customer_id, age, gender, income_level, loyalty_program_status, clv, purchase_frequency, 
        avg_basket_size, purchase_method, first_purchase_date, last_purchase_date, satisfaction_score,
        product_name, category, product_price, brand, product_type, product_size, product_color, 
        product_rating, stock_level, restock_date, supplier_id, product_lifecycle_stage, product_description, 
        shipping_weight, return_rate, promotions, holidays, competitor_pricing, competitor_promotions, market_trend, 
        weather, local_events, economic_conditions, advertising_spend, social_media_sentiment, 
        competitor_product_launch, pricing_changes, shipping_promotions
    ])

# Create DataFrames
sales_columns = [
    'Store ID', 'Product ID', 'Date', 'Units Sold', 'Revenue', 'Discount', 'Sales Channel', 'Store Location', 
    'Store Type', 'Time of Sale', 'Seasonality Indicator', 'Stock Availability', 'Sales Representative',
    'Customer ID', 'Age', 'Gender', 'Income Level', 'Loyalty Program Status', 'Customer Lifetime Value (CLV)', 
    'Purchase Frequency', 'Average Basket Size', 'Purchase Method', 'First Purchase Date', 'Last Purchase Date', 
    'Customer Satisfaction Score', 'Product Name', 'Category', 'Price', 'Brand', 'Product Type', 'Product Size', 
    'Product Color', 'Product Rating', 'Stock Level', 'Restock Date', 'Supplier ID', 'Product Lifecycle Stage', 
    'Product Description', 'Shipping Weight', 'Return Rate', 'Promotions', 'Holidays', 'Competitor Pricing', 
    'Competitor Promotions', 'Market Trend', 'Weather', 'Local Events', 'Economic Conditions', 'Advertising Spend', 
    'Social Media Sentiment', 'Competitor Product Launch', 'Pricing Changes', 'Shipping Promotions'
]

store_columns = ['Store ID', 'Store Name', 'Store Location', 'Store Type', 'Store Size', 'Store Manager']
product_columns = ['Product ID', 'Product Name', 'Category', 'Price', 'Product Type', 'Brand', 'Description', 
                   'Stock Level', 'Supplier ID']

sales_df = pd.DataFrame(data, columns=sales_columns)
store_df = pd.DataFrame(store_data, columns=store_columns)
product_df = pd.DataFrame(product_data, columns=product_columns)

# Write data to Excel
with pd.ExcelWriter('sales_forecasting_with_store_and_product_details.xlsx') as writer:
    sales_df.to_excel(writer, sheet_name='Sales Data', index=False)
    store_df.to_excel(writer, sheet_name='Store Details', index=False)
    product_df.to_excel(writer, sheet_name='Product Details', index=False)

print("Sales, Store, and Product data created and saved successfully in Excel file!")
