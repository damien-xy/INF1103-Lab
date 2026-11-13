""" Lab 8 - Liskov Substitution Principle Test """

# -----------------------------------
# imports
# -----------------------------------
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

# -----------------------------------
# functions
# -----------------------------------
def show_product_details(product: Product) -> None:
    """ displays product details using the Product abstraction """

    product.display_information()
    print(product.get_fulfilment_info())

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    # create supplier
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # create physical and digital products
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)
    product2 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)

    # test substitutability using the Product abstraction
    print("Physical Product:")
    show_product_details(product1)

    print("\nDigital Product:")
    show_product_details(product2)

    # test both product types in Inventory
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)

    print("\nTesting Inventory with Both Product Types:")
    inventory.display_all()
