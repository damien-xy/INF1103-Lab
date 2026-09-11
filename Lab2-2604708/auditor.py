""" Lab 2 - Smart Inventory Auditor """

# initialise to 0
inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity or type 'quit': ").strip()

    # stop program if user types 'quit'
    if user_input.lower() == "quit":
        break

    # handle invalid inputs (string / negative )
    if not user_input.isdigit():
        print("[ERROR] Invalid input. Please enter a valid integer.")
        failed_entries += 1
        continue

    # convert input to integer
    new_inventory = int(user_input)

    # update inventory
    inventory = inventory + new_inventory

    # check inventory for overstock (> 500)
    if inventory > 500:
        print("[WARNING] Total Inventory has exceeded 500 units.")
        break

# reporting
print("\n--------- Inventory Report ---------")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
