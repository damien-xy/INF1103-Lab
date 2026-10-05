""" Lab 5 - Inventory Management System """

# -----------------------------------
# imports
# -----------------------------------
import json
from pathlib import Path

# -----------------------------------
# file paths
# -----------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = SCRIPT_DIR / "inventory.json"

# -----------------------------------
# input validation
# -----------------------------------
def get_valid_product_id(prompt="Product ID: "):
    """ gets and validates a product ID """

    while True:
        product_id = input(prompt).strip().upper()

        if (len(product_id) == 4 and product_id[0] == "P" and product_id[1:].isdigit()):
            return product_id

        print("[ERROR] Product ID must be in the format P001.")

def get_valid_product_name():
    """ gets, sanitises and validates a product name """

    while True:
        product_name = " ".join(input("Product Name: ").split())

        # check that name is not empty and contains at least one letter
        if product_name and any(char.isalpha() for char in product_name):
            return product_name.title()

        print("[ERROR] Product name must contain at least one letter.")

def get_valid_price():
    """ gets and validates a product price """

    while True:
        price_input = input("Price: ").strip()

        try:
            price = float(price_input)

            if price >= 0:
                return price

            print("[ERROR] Price cannot be negative.")

        except ValueError:
            print("[ERROR] Price must be a valid number.")

def get_valid_stock(prompt="Stock Quantity: "):
    """ gets and validates a product stock quantity """

    while True:
        stock_input = input(prompt).strip()

        try:
            stock = int(stock_input)

            if stock >= 0:
                return stock

            print("[ERROR] Stock quantity cannot be negative.")

        except ValueError:
            print("[ERROR] Stock quantity must be a whole number.")

# -----------------------------------
# functions
# -----------------------------------
def load_inventory():
    """ loads inventory data from inventory.json """

    if INVENTORY_FILE.exists():
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            inventory_data = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory_data

    print("inventory.json not found.")
    return []

def save_inventory(inventory):
    """ saves inventory data to inventory.json """

    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def display_all(inventory):
    """ displays all products in the inventory """

    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("------------------------------------------------")

def add_product(inventory):
    """ adds a new product to the inventory """

    print("\nAdd New Product")

    while True:
        product_id = get_valid_product_id()

        if any(product["id"] == product_id for product in inventory):
            print("[ERROR] Product ID already exists.")
        else:
            break
    product_name = get_valid_product_name()
    price = get_valid_price()
    stock = get_valid_stock()

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")

def update_stock(inventory):
    """ updates the stock quantity of an existing product """

    print("\nUpdate Stock")

    product_id = get_valid_product_id("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = get_valid_stock("New Stock Quantity: ")
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

def search_product(inventory):
    """ searches for a product by product ID """

    print("\nSearch Product")

    product_id = get_valid_product_id("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")
            return

    print("Product not found.")

def display_menu():
    """ displays the inventory management menu """

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

# -----------------------------------
# main
# -----------------------------------
inventory = load_inventory()

while True:
    display_menu()

    option = input("Enter option: ").strip()

    if option == "1":
        display_all(inventory)
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)
    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 6.")
