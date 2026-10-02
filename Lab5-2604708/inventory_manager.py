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
# initial inventory
# - based on Lab 5 screenshots
#   ID: P001 | Name: Laptop | Price: $1200.00 | Stock: 15
#   ID: P002 | Name: Mouse | Price: $25.50 | Stock: 40
#   ID: P003 | Name: Keyboard | Price: $45.00 | Stock: 2
# -----------------------------------
initial_inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 2
    }
]

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
    else:
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

    product_id = input("Product ID: ").strip()
    product_name = input("Product Name: ").strip()
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

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

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

def search_product(inventory):
    """ searches for a product by product ID """

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

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
