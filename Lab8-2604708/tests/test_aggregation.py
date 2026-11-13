
""" Lab 8 - Aggregation Test """

# -----------------------------------
# imports
# -----------------------------------
from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    # create supplier and product
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)

    # create two inventories
    inventory_a = Inventory()
    inventory_b = Inventory()

    # add product to Inventory A
    inventory_a.add_product(product1)

    print("Inventory A before removal:")
    inventory_a.display_all()

    # remove product from Inventory A
    inventory_a.remove_product("P004")

    print("\nInventory A after removal:")
    inventory_a.display_all()

    # test whether product still exists
    print("\nProduct after removal:")
    product1.display_information()

    # add the same product to Inventory B
    inventory_b.add_product(product1)

    print("\nInventory B after transfer:")
    inventory_b.display_all()

    # check whether it is the same Product object
    print("\nSame Product object:", inventory_b.find_product("P004") is product1)
