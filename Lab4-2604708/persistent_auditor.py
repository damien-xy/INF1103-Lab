""" Lab 4 -  Persistent Modular Smart Inventory Auditor """

# -----------------------------------
# imports
# -----------------------------------
from datetime import datetime
from pathlib import Path

# -----------------------------------
# file paths
# -----------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = SCRIPT_DIR / "inventory.txt"

# -----------------------------------
# functions
# -----------------------------------
def get_valid_input():
    """ 
        handles the prompt and input validation 
        returns a valid integer or a "quit" signal
    """
    user_input = input("Enter stock quantity or type 'quit': ").strip()

    # return 'quit' if user types 'quit'
    if user_input.lower() == "quit":
        return "quit"

    # return None if invalid input (string / negative)
    if not user_input.isdigit():
        print("[ERROR] Invalid input. Please enter a valid integer.\n")
        return None

    # return input as integer
    return int(user_input)

def process_delivery(current_total, new_value):
    """ calculates the new total and returns it """
    new_total = current_total + new_value

    return new_total

def calculate_tax(amount):
    """  takes a delivery amount and returns the 10% tax """

    return amount * 0.10

def generate_report(total_units, failed_attempts):
    """ prints final inventory report """
    print("\n--------- Inventory Report ---------")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

def load_inventory():
    """ loads inventory from inventory.txt """
    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            # read all non-empty lines
            lines = [line.strip() for line in file if line.strip()]

            # return empty inventory if file is empty
            if not lines:
                return 0, []

            # get latest total inventory
            inventory_line = lines[-2]
            inventory = int(inventory_line.split(":", 1)[1].strip())

            # get latest transaction history
            transaction_line = lines[-1]
            transaction_text = transaction_line.split(":", 1)[1].strip()

            if transaction_text:
                transaction_history = [
                    int(value.strip())
                    for value in transaction_text.split(",")
                ]
            else:
                transaction_history = []

            return inventory, transaction_history

    except FileNotFoundError:
        # start with empty inventory if file does not exist
        return 0, []

def save_inventory(updated_inventory, transaction_history):
    """ saves inventory to inventory.txt"""

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(INVENTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"--------- Inventory Report for {timestamp} ---------\n")
        file.write(f"Total Inventory: {updated_inventory}\n")
        file.write(f"Transactions: {', '.join(str(value) for value in transaction_history)}\n\n")

# -----------------------------------
# main
# -----------------------------------
# load inventory
inventory, history = load_inventory()

# initialise failed_entries to 0
failed_entries = 0

while True:
    new_inventory = get_valid_input()

    if new_inventory == "quit":
        save_inventory(inventory, history)
        break

    if new_inventory is None:
        failed_entries += 1
        continue

    # update inventory
    inventory = process_delivery(inventory, new_inventory)

    # update valid transaction in history
    history.append(new_inventory)

    # calculate tax for this delivery
    tax = calculate_tax(new_inventory)
    print(f"Tax for this delivery: {tax:.2f}\n")

    # check inventory for overstock (> 500)
    if inventory > 500:
        print("[WARNING] Total Inventory has exceeded 500 units.")
        save_inventory(inventory, history)
        break

# reporting
generate_report(inventory, failed_entries)
