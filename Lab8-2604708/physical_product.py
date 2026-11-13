
""" Lab 7 - PhysicalProduct Class """

# -----------------------------------
# imports
# -----------------------------------
from product import Product
from can_be_shipped import CanBeShipped

# -----------------------------------
# classes
# -----------------------------------
class PhysicalProduct(Product, CanBeShipped):
    """ represents a physical product with weight """

    def __init__(self, product_id, name, price, stock, weight):
        """ initialises a physical product with its weight """

        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        """ displays product information including weight """

        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        """ returns physical product fulfilment information """

        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        """ calculates shipping cost based on product weight """

        return self.__weight * 2.00

    def to_dict(self):
        """ returns physical product information as a dictionary """

        product_data = super().to_dict()
        product_data["type"] = "physical"
        product_data["weight"] = self.__weight

        return product_data

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5)
    product2 = PhysicalProduct("P006", "Laptop", 1299.99, 10, 1.5)

    # test displaying physical product information
    product1.display_information()

    # test fulfilment information
    print(product1.get_fulfilment_info())

    # test shipping cost calculation with different weights
    print(f"\nProduct 1 Shipping Cost: ${product1.calculate_shipping_cost():.2f}")
    print(f"Product 2 Shipping Cost: ${product2.calculate_shipping_cost():.2f}")

    # test converting physical product to dictionary
    print("\nTesting to_dict():")
    print(product1.to_dict())
