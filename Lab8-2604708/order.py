""" Lab 8 - Order Class """

# -----------------------------------
# imports
# -----------------------------------
from product import Product
from order_line import OrderLine

# -----------------------------------
# classes
# -----------------------------------
class Order:
    """ represents an order containing order lines """

    def __init__(self, order_id: str) -> None:
        """ initialises an order with an empty list of order lines """

        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """ creates and adds an order line to the order """

        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        """ calculates the total value of the order """

        return sum(order_line.calculate_subtotal() for order_line in self.__order_lines)
