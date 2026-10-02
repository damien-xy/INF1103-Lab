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
inventory = [
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
