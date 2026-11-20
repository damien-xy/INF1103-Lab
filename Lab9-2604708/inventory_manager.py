""" Lab 9 - OOP Inventory Management System """

# -----------------------------------
# imports
# -----------------------------------
import json
from pathlib import Path

from classes.inventory import Inventory
from classes.supplier import Supplier
from classes.product_factory import ProductFactory

# -----------------------------------
# file paths
# -----------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = SCRIPT_DIR / "inventory.json"

# -----------------------------------
# input validation
# -----------------------------------
def get_valid_product_id(prompt: str = "Product ID: ") -> str:
    """ gets and validates a product ID """

    while True:
        product_id = input(prompt).strip().upper()

        if (len(product_id) == 4 and product_id[0] == "P" and product_id[1:].isdigit()):
            return product_id

        print("[ERROR] Product ID must be in the format P001.")

def get_valid_product_name() -> str:
    """ gets, sanitises and validates a product name """

    while True:
        product_name = " ".join(input("Product Name: ").split())

        # check that name is not empty and contains at least one letter
        if product_name and any(char.isalpha() for char in product_name):
            return product_name.title()

        print("[ERROR] Product name must contain at least one letter.")

def get_valid_price() -> float:
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

def get_valid_stock(prompt: str = "Stock Quantity: ") -> int:
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

def get_valid_non_negative_float(prompt: str) -> float:
    """ gets and validates a non-negative decimal number """

    while True:
        value_input = input(prompt).strip()

        try:
            value = float(value_input)

            if 0 <= value < float("inf"):
                return value

            print("[ERROR] Value must be a non-negative number.")

        except ValueError:
            print("[ERROR] Please enter a valid number.")

# -----------------------------------
# functions
# -----------------------------------
def load_inventory() -> Inventory:
    """ loads inventory data from inventory.json into an Inventory object """

    inventory = Inventory()

    if INVENTORY_FILE.exists():
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            inventory_data = json.load(file)

        for product_data in inventory_data:
            product_type = product_data["type"]

            # reconstruct supplier object
            supplier_data = product_data["supplier"]

            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"]
            )

            try:
                product = ProductFactory.create(
                    product_type,
                    product_data["id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    supplier,
                    weight=product_data.get("weight", 0.0),
                    download_size=product_data.get("download_size", 0.0)
                )

            except ValueError as e:
                print(f"[WARNING] {e}")
                continue

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found.")
        print("Creating a new inventory.json...")

        save_inventory(inventory)

    return inventory

def save_inventory(inventory: Inventory) -> None:
    """ saves inventory data to inventory.json """

    inventory_data = inventory.to_dict_list()

    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(inventory_data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def add_product(inventory: Inventory) -> None:
    """ adds a new physical or digital product to the inventory """

    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    # get product type
    while True:
        product_type = input("Select Product Type: ").strip()

        if product_type in ("1", "2"):
            break

        print("[ERROR] Please select 1 or 2.")

    # get unique product ID
    while True:
        product_id = get_valid_product_id()

        if inventory.search_product(product_id) is not None:
            print("[ERROR] Product ID already exists.")
        else:
            break

    # get common product information
    product_name = get_valid_product_name()
    price = get_valid_price()
    stock = get_valid_stock()

    # get supplier information
    print("\nSupplier Information")

    supplier_id = input("Supplier ID: ").strip().upper()
    supplier_name = " ".join(input("Supplier Name: ").split()).title()
    supplier_email = input("Supplier Email: ").strip()

    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    # create the appropriate product type using ProductFactory
    if product_type == "1":
        weight = get_valid_non_negative_float("Weight (kg): ")

        new_product = ProductFactory.create(
            "physical", product_id, product_name, price, stock,
            supplier, weight=weight
        )

    else:
        download_size = get_valid_non_negative_float("Download Size (MB): ")

        new_product = ProductFactory.create(
            "digital", product_id, product_name, price, stock,
            supplier, download_size=download_size
        )

    inventory.add_product(new_product)

    print("Product added successfully!")

def update_stock(inventory: Inventory) -> None:
    """ updates the stock quantity of an existing product """

    print("\nUpdate Stock")

    product_id = get_valid_product_id("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if product is not None:
        print("Product Found:")
        product.display_information()

        new_stock = get_valid_stock("New Stock Quantity: ")
        product.update_stock(new_stock)

        print("Stock updated successfully!")

    else:
        print("Product not found.")

def search_product(inventory: Inventory) -> None:
    """ searches for a product by product ID """

    print("\nSearch Product")

    product_id = get_valid_product_id("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if product is not None:
        print("Product Found")
        print("------------------------------------------------")
        product.display_information()
        print("------------------------------------------------")

    else:
        print("Product not found.")

def display_menu() -> None:
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
def main() -> None:
    """ runs the inventory management system """

    inventory = load_inventory()

    while True:
        display_menu()

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()
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

if __name__ == "__main__":
    main()
