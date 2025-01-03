
# Problem Statement:
# Create an inventory management system for a store that categorizes products and 
# calculates discounts based on the product type. The system will need to handle 
# products in three categories: Electronics, Clothing, and Books. 
# It will also need to apply specific discounts to each category of product, 
# and maintain a list of products in the store's inventory.


# ### Level 1: Base Class - Product
# In this level, define the `Product` class which will serve as the base 
# class for all products. The `Product` class will have the following attributes:
# - `name`: The name of the product.
# - `price`: The price of the product.
# - `product_id`: A unique identifier for the product.
# - A method `apply_discount()` to apply a discount to the price of the product.
# - A `__str__()` method to return a string representation of the product.


class Product:
    """Base class for all products."""
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def apply_discount(self, discount):
        """Apply a discount to the product's price."""
        self.price -= self.price * (discount / 100)
        return self.price

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}"



### Level 2: Derived Classes - Electronics, Clothing, Books
#### Hierarchical Inheritance: Electronics and Clothing inherit directly from `Product`
# In this level, we will create the derived classes `Electronics` and `Clothing` 
# that inherit from `Product`. Additionally, we will also create 
# `Books` class which will be based on multilevel inheritance.

# 1. Electronics Class:
#    - Additional attributes: `warranty`, `brand`.
#    - Overrides `__str__()` to display additional information.
   
# 2. Clothing Class:
#    - Additional attributes: `size`, `material`.
#    - Overrides `__str__()` to display additional information.

# 3. Books Class:
#    - Additional attributes: `author`, `genre`.
#    - Overrides `__str__()` to display additional information.


# Electronics Class
class Electronics(Product):
    """Derived class for electronics."""
    def __init__(self, name, price, product_id, warranty, brand):
        super().__init__(name, price, product_id)
        self.warranty = warranty
        self.brand = brand

    def __str__(self):
        return super().__str__() + f", Brand: {self.brand}, Warranty: {self.warranty} years"

# Clothing Class
class Clothing(Product):
    """Derived class for clothing."""
    def __init__(self, name, price, product_id, size, material):
        super().__init__(name, price, product_id)
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Material: {self.material}"

# Books Class
class Books(Product):
    """Derived class for books."""
    def __init__(self, name, price, product_id, author, genre):
        super().__init__(name, price, product_id)
        self.author = author
        self.genre = genre

    def __str__(self):
        return super().__str__() + f", Author: {self.author}, Genre: {self.genre}"



# ### Level 3: Inventory Management System
# The `Inventory` class will handle a list of products, allowing 
# for adding products to the inventory, displaying the products, 
# and applying discounts based on the type of product.

# - `add_product(product)`: Adds a product to the inventory.
# - `display_products()`: Displays all products in the inventory.
# - `apply_discounts()`: Applies different discounts based on the product type.


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products:
                print(product)

    def apply_discounts(self):
        """Apply specific discounts based on product type."""
        for product in self.products:
            if isinstance(product, Electronics):
                product.apply_discount(10)  # 10% discount for electronics
            elif isinstance(product, Clothing):
                product.apply_discount(20)  # 20% discount for clothing
            elif isinstance(product, Books):
                product.apply_discount(5)  # 5% discount for books



# ### Level 4: Example Usage
# In this level, you will create instances of products, add them to the inventory, 
# display the products before and after applying discounts, 
# and see how the system works.


if __name__ == "__main__":
    inventory = Inventory()

    laptop = Electronics("Laptop", 1500, 101, 2, "Dell")
    tshirt = Clothing("T-shirt", 25, 102, "M", "Cotton")
    book = Books("Python Programming", 45, 103, "John Doe", "Education")

    inventory.add_product(laptop)
    inventory.add_product(tshirt)
    inventory.add_product(book)
    print("Products before applying discounts:")
    inventory.display_products()
    inventory.apply_discounts()
    print("\nProducts after applying discounts:")
    inventory.display_products()


