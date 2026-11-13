""" Lab 8 - Polymorphism Test """

# -----------------------------------
# imports
# -----------------------------------
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    # create supplier
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # create physical and digital products
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)
    product2 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)

    # create inventory and add both products
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)

    # test polymorphism through the Product collection
    print("Testing Polymorphism:")

    for product in inventory.get_products():
        print()
        product.display_information()
        print(product.get_fulfilment_info())
