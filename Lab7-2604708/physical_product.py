
""" Lab 7 - Physical Product Class """

# -----------------------------------
# imports
# -----------------------------------
from product import Product

# -----------------------------------
# classes
# -----------------------------------
class PhysicalProduct(Product):
    """ represents a physical product with weight """

    def __init__(self, product_id, name, price, stock, weight):
        """ initialises a physical product with its weight """

        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        """ displays product information including weight """

        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5)

    # test displaying physical product information
    product1.display_information()
