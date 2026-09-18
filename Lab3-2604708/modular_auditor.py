""" Lab 3 - Modular Smart Inventory Auditor """

# -----------------------------------
# functions
# -----------------------------------
def get_valid_input():
    """ 
        handles the prompt and input validation 
        returns a valid integer or a "quit" signal
    """
    user_input = input("Enter stock quantity or type 'quit': ").strip()

    # stop program if user types 'quit'
    if user_input.lower() == "quit":
        return "quit"

    # handle invalid inputs (string / negative)
    if not user_input.isdigit():
        print("[ERROR] Invalid input. Please enter a valid integer.")
        return None

    # return input as integer
    return int(user_input)

def process_delivery(current_total, new_value):
    """ calculates the new total and returns it """
    new_total = current_total + new_value

    return new_total

def calculate_tax(amount):
    """  takes a delivery amount and returns the 10% tax """

def generate_report(total_units, failed_attempts):
    """ prints final inventory report """

# -----------------------------------
# main
# -----------------------------------
# initialise to 0
inventory = 0
failed_entries = 0

while True:
    new_inventory = get_valid_input()

    if new_inventory == "quit":
        break

    if new_inventory is None:
        failed_entries += 1
        continue

    # update inventory
    inventory = process_delivery(inventory, new_inventory)

    # check inventory for overstock (> 500)
    if inventory > 500:
        print("[WARNING] Total Inventory has exceeded 500 units.")
        break

# reporting
print("\n--------- Inventory Report ---------")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
