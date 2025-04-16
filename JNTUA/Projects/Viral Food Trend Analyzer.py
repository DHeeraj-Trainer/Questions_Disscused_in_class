import pandas as pd
import numpy as np
import random
import faker

# Initialize the Faker library for generating fake data
fake = faker.Faker()

# Function to generate random social media data
def generate_social_media_data(num_rows):
    platforms = ['TikTok', 'Instagram', 'YouTube', 'Facebook', 'Twitter']
    dishes = [
    'Avocado Toast', 'Vegan Burger', 'Sushi Rolls', 'Cauliflower Tacos', 'Poke Bowl', 
    'Spaghetti Bolognese', 'Acai Bowl', 'Matcha Latte', 'Loaded Fries', 'Boba Tea',
    'Smoothie Bowl', 'Mushroom Risotto', 'Chickpea Salad', 'Vegan Tacos', 'Eggplant Parmesan',
    'Vegan Pizza', 'Pad Thai', 'Vegan Curry', 'Grilled Portobello', 'Tofu Stir Fry', 
    'Cauliflower Wings', 'Kale Caesar Salad', 'Zucchini Noodles', 'Chia Pudding', 'Coconut Rice',
    'Falafel Wrap', 'Vegan Burrito', 'Avocado Salad', 'Stuffed Bell Peppers', 'Jackfruit Tacos',
    'Vegan Sushi', 'Lentil Soup'
]
    hashtags = [
    '#Foodie', '#ViralEats', '#HealthyFood', '#Tasty', '#FoodPorn', '#VeganLife', '#KetoRecipes', 
    '#Foodstagram', '#InstaFood', '#RecipeOfTheDay', '#PlantBased', '#VeganEats', '#FoodLover', 
    '#HealthyEating', '#CleanEating', '#MealPrep', '#Yummy', '#FoodIsLife', '#WhatILoveToEat', 
    '#VegansOfInstagram', '#FoodCravings', '#VeganRecipes', '#VeganFoodPorn', '#VeggieDelight', 
    '#FoodPics', '#Delicious', '#EatClean', '#HealthyChoices', '#InstaGood', '#TastyEats', 
    '#NomNom', '#FoodGoals', '#FoodForThought', '#VeganTreats'
]
    
    social_data = []
    
    for _ in range(num_rows):
        platform = random.choice(platforms)
        hashtag = random.choice(hashtags)
        engagement_likes = random.randint(500, 20000)
        engagement_shares = random.randint(100, 10000)
        engagement_comments = random.randint(50, 3000)
        post_date = fake.date_this_year()
        influencer_name = fake.name()
        followers = random.randint(1000, 500000)
        engagement_rate = round(random.uniform(0.01, 0.1), 3)
        video_views = random.randint(1000, 500000) if platform in ['TikTok', 'YouTube'] else 0
        content_type = random.choice(['Image', 'Video', 'Reel', 'Story', 'Live Stream'])
        
        social_data.append([platform, hashtag, engagement_likes, engagement_shares, engagement_comments, post_date, influencer_name, followers, engagement_rate, video_views, content_type])
        
    return social_data

# Function to generate random sales data
def generate_sales_data(num_rows):
    restaurant_names = [
    'Tasty Bites', 'Green Table', 'Sushi King', 'Vegan Haven', 'Pasta Palace', 'Boba Express',
    'Chaat Street', 'Spicy Feast', 'Curry Bliss', 'Masala Magic', 'Dosa Delight', 'Sitar Restaurant',
    'The Bombay Café', 'The Vegan Café', 'Tandoor Express', 'Urban Spice', 'The Spice House', 
    'Biryani Pot', 'Saffron Soul', 'The Pani Puri Place', 'Sushi & Sambar', 'The Naan Lab',
    'Vegan Vibes', 'Bengal Bites', 'Vibrant Veggie', 'Momos & More', 'Tandoori Treats', 
    'Kebab Corner', 'Roti Rolls', 'Kathi Wrap Kitchen', 'The Falafel Shack', 'Indo-Mexican Fusion', 
    'Veggie Treats', 'Royal Rasoi', 'Samosa House', 'Masala Dosa Café', 'Curry Cart', 
    'Gulab Jamun Delights', 'Biryani Baithak', 'The Curry Leaf', 'Pav Bhaji Café', 'Sambar Express',
    'The Vegan Lotus', 'Spice Junction', 'Dosa Delight', 'Tandoor Tastes', 'Kolkata Kafe', 
    'Amritsari Treats', 'Pind Punjabi', 'Delhi Diner', 'Street Food Mania', 'Rajasthani Royalty'
]
    dishes = [
    'Avocado Toast', 'Vegan Burger', 'Sushi Rolls', 'Cauliflower Tacos', 'Poke Bowl', 
    'Spaghetti Bolognese', 'Acai Bowl', 'Matcha Latte', 'Loaded Fries', 'Boba Tea',
    'Smoothie Bowl', 'Mushroom Risotto', 'Chickpea Salad', 'Vegan Tacos', 'Eggplant Parmesan',
    'Vegan Pizza', 'Pad Thai', 'Vegan Curry', 'Grilled Portobello', 'Tofu Stir Fry', 
    'Cauliflower Wings', 'Kale Caesar Salad', 'Zucchini Noodles', 'Chia Pudding', 'Coconut Rice',
    'Falafel Wrap', 'Vegan Burrito', 'Avocado Salad', 'Stuffed Bell Peppers', 'Jackfruit Tacos',
    'Vegan Sushi', 'Lentil Soup', 'Chana Masala', 'Aloo Tikki', 'Pav Bhaji', 'Vegan Butter Chicken',
    'Vegan Saag Paneer', 'Vegetable Biryani', 'Vegan Korma', 'Aloo Gobi', 'Chole Bhature', 
    'Vegan Samosas', 'Dosas', 'Vegan Tandoori', 'Vegan Pulao', 'Methi Thepla', 'Vegan Keema',
    'Vegan Pakoras', 'Vegan Kachori', 'Vegan Lassi', 'Vegan Malai Kofta', 'Vegan Dhokla',
    'Vegan Poha', 'Vegan Vada Pav', 'Bhindi Masala'
]
    locations = [
    'New York', 'Los Angeles', 'Chicago', 'Austin', 'Miami', 'San Francisco',
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 'Pune', 'Ahmedabad', 
    'Jaipur', 'Lucknow', 'Chandigarh', 'Kochi', 'Goa', 'Varanasi', 'Indore', 'Nagpur', 'Surat', 
    'Bhopal', 'Kochi', 'Mysuru', 'Vadodara', 'Rishikesh', 'Nashik', 'Udaipur', 'Pondicherry', 
    'Shimla', 'Darjeeling', 'Agra', 'Coimbatore', 'Raipur', 'Jodhpur', 'Dehradun', 'Gurugram', 
    'Noida', 'Thane', 'Ghaziabad', 'Faridabad', 'Chandrapur', 'Mangalore', 'Trivandrum', 
    'Kanpur', 'Vijayawada', 'Dhanbad', 'Tiruchirappalli', 'Kottayam', 'Bhubaneswar', 'Siliguri', 
    'Patna', 'Jammu', 'Bikaner', 'Amritsar', 'Madurai', 'Kozhikode', 'Rajkot', 'Gwalior'
]
    
    sales_data = []
    
    for _ in range(num_rows):
        restaurant = random.choice(restaurant_names)
        dish = random.choice(dishes)
        sales_volume = random.randint(50, 1000)
        date = fake.date_this_year()
        location = random.choice(locations)
        dish_price = round(random.uniform(5, 20), 2)
        
        sales_data.append([restaurant, dish, sales_volume, date, location, dish_price])
        
    return sales_data

# Function to generate random recipe data
def generate_recipe_data(num_rows):
    dishes = ['Avocado Toast', 'Vegan Burger', 'Sushi Rolls', 'Cauliflower Tacos', 'Poke Bowl', 'Spaghetti Bolognese', 'Acai Bowl', 'Matcha Latte', 'Loaded Fries', 'Boba Tea']
    cuisines = ['American', 'Japanese', 'Mexican', 'Vegan', 'Italian']
    preparation_time = [10, 15, 20, 30, 45]
    dietary_restrictions = ['None', 'Vegan', 'Gluten-Free', 'Dairy-Free', 'Keto']
    
    recipe_data = []
    
    for _ in range(num_rows):
        dish = random.choice(dishes)
        ingredients = ', '.join([fake.word() for _ in range(random.randint(4, 10))])
        prep_time = random.choice(preparation_time)
        cuisine = random.choice(cuisines)
        servings = random.randint(1, 5)
        dietary = random.choice(dietary_restrictions)
        calories = random.randint(100, 800)
        
        recipe_data.append([dish, ingredients, prep_time, cuisine, servings, dietary, calories])
        
    return recipe_data

# Function to introduce errors in the data (20% error rate)
def introduce_errors(df, error_rate=0.2):
    # Introduce missing data (NaN) in random cells
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            # Introduce NaN for 20% of the entries in numerical columns
            num_missing = int(len(df) * error_rate)
            missing_indices = random.sample(range(len(df)), num_missing)
            df.loc[missing_indices, col] = np.nan

            # Introduce outliers in 5% of the data (higher or lower than the range)
            num_outliers = int(len(df) * 0.05)
            outlier_indices = random.sample(range(len(df)), num_outliers)
            if df[col].dtype == 'int64' or df[col].dtype == 'float64':
                # Adding outliers
                df.loc[outlier_indices, col] = df[col].mean() + random.choice([-10, 10]) * df[col].std()
    
    return df

# Function to generate unique IDs for dishes, restaurants, and influencers
def generate_unique_ids(df, column_name):
    unique_items = df[column_name].unique()
    id_mapping = {item: idx for idx, item in enumerate(unique_items, start=1)}
    df[f'{column_name}_ID'] = df[column_name].map(id_mapping)
    return df

# Generate the 10,000 rows of data
num_rows = 10000

social_media_data = generate_social_media_data(num_rows)
sales_data = generate_sales_data(num_rows)
recipe_data = generate_recipe_data(num_rows)

# Create DataFrames for each dataset
columns_social = [
    'Platform', 'Hashtag', 'Engagement Likes', 'Engagement Shares', 'Engagement Comments', 
    'Post Date', 'Influencer Name', 'Followers', 'Engagement Rate', 'Video Views', 'Content Type'
]

columns_sales = [
    'Restaurant Name', 'Dish Name', 'Sales Volume', 'Date', 'Location', 'Dish Price'
]

columns_recipe = [
    'Dish Name', 'Ingredients', 'Preparation Time', 'Cuisine Type', 'Servings', 'Dietary Restrictions', 'Calories'
]

social_df = pd.DataFrame(social_media_data, columns=columns_social)
sales_df = pd.DataFrame(sales_data, columns=columns_sales)
recipe_df = pd.DataFrame(recipe_data, columns=columns_recipe)

# Add IDs for dishes, restaurants, and influencers
social_df = generate_unique_ids(social_df, 'Influencer Name')
sales_df = generate_unique_ids(sales_df, 'Restaurant Name')
recipe_df = generate_unique_ids(recipe_df, 'Dish Name')

# Combine all data into one DataFrame for cleaning
combined_df = pd.concat([social_df, sales_df, recipe_df], ignore_index=True)

# Introduce errors in the combined data
combined_df_with_errors = introduce_errors(combined_df, error_rate=0.2)

# Save the final DataFrame to an Excel file with separate sheets for each dataset
file_path_with_ids = 'viral_food_trends_with_ids.xlsx'
with pd.ExcelWriter(file_path_with_ids, engine='xlsxwriter') as writer:
    social_df.to_excel(writer, sheet_name='Social Media Data', index=False)
    sales_df.to_excel(writer, sheet_name='Sales Data', index=False)
    recipe_df.to_excel(writer, sheet_name='Recipe Data', index=False)
    combined_df_with_errors.to_excel(writer, sheet_name='Combined Data with Errors', index=False)

print("Excel file with IDs and Errors has been saved successfully.")
