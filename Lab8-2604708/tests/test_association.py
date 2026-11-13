""" Lab 8 - Association Test """

# -----------------------------------
# imports
# -----------------------------------
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    # create supplier
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # create products using the same supplier
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)
    product2 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)

    # display supplier information before deletion
    print("Before deleting supplier:")
    supplier.display_information()

    # delete the supplier variable
    del supplier

    # test accessing supplier information after deletion
    print("\nAfter deleting supplier:")

    print("\nPhysical Product Supplier:")
    product1.display_supplier_information()

    print("\nDigital Product Supplier:")
    product2.display_supplier_information()
