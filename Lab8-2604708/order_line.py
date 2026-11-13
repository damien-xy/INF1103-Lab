""" Lab 8 - OrderLine Class """

# -----------------------------------
# imports
# -----------------------------------
from product import Product

# -----------------------------------
# classes
# -----------------------------------
class OrderLine:
    """ represents a product and its quantity in an order """

    def __init__(self, product: Product, quantity: int) -> None:
        """ initialises an order line with a product and quantity """

        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """ calculates the subtotal for the order line """

        return self.__product.get_price() * self.__quantity
