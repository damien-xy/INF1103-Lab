""" Lab 8 - Composition Test """

# -----------------------------------
# imports
# -----------------------------------
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    # create supplier and product
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)

    # create two orders
    order1 = Order("O001")
    order2 = Order("O002")

    # add the same product to both orders
    order1.add_order_line(product1, 2)
    order2.add_order_line(product1, 3)

    # display both orders
    print("Order 1:")
    order1.display_order_lines()
    print(f"Order Total: ${order1.calculate_total():.2f}")

    print("\nOrder 2:")
    order2.display_order_lines()
    print(f"Order Total: ${order2.calculate_total():.2f}")

    # show that the same product object was reused
    print(f"\nOriginal Product Object ID: {id(product1)}")

    # add another product to Order 1
    product2 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)
    order1.add_order_line(product2, 1)

    print("\nOrder 1 after adding another product:")
    order1.display_order_lines()
    print(f"Updated Order Total: ${order1.calculate_total():.2f}")

    # remove Order 2
    del order2

    # confirm the original product still exists
    print("\nProduct after deleting Order 2:")
    product1.display_information()
