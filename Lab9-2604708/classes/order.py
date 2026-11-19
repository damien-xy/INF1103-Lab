""" Lab 9 - Order Class """

# -----------------------------------
# imports
# -----------------------------------
from .product import Product
from .order_line import OrderLine
from .discount_strategy import DiscountStrategy
from .no_discount import NoDiscount

# -----------------------------------
# classes
# -----------------------------------
class Order:
    """ represents an order containing order lines """

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        """ initialises an order with an empty list of order lines and a discount strategy """

        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        """ creates and adds an order line to the order """

        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        """ updates the discount strategy used by the order """

        self.__discount = discount

    def calculate_total(self) -> float:
        """ calculates the total value of the order after applying the discount """

        total = sum(order_line.calculate_subtotal() for order_line in self.__order_lines)
        return self.__discount.apply(total)

    def display_order_lines(self) -> None:
        """ displays all order lines in the order """

        print(f"\nOrder ID: {self.__order_id}")

        for index, order_line in enumerate(self.__order_lines, start=1):
            print(f"\nOrder Line {index}:")
            order_line.display_information()

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    from .supplier import Supplier
    from .physical_product import PhysicalProduct
    from .bulk_discount import BulkDiscount
    from .percentage_discount import PercentageDiscount

    supplier = Supplier("S001", "Test Supplier", "test@example.com")
    product = PhysicalProduct("P001", "Test Product", 125.0, 10, 1.0, supplier)

    # create an order with a bulk discount
    order = Order("O001", BulkDiscount(200, 20))
    order.add_order_line(product, 2)

    print(f"Bulk Discount Total: {order.calculate_total()}")

    # change the discount strategy to percentage discount
    order.set_discount(PercentageDiscount(10))

    print(f"Percentage Discount Total: {order.calculate_total()}")
