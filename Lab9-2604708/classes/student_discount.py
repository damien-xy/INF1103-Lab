""" Lab 9 - StudentDiscount Class """

# -----------------------------------
# imports
# -----------------------------------
from .discount_strategy import DiscountStrategy

# -----------------------------------
# classes
# -----------------------------------
class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    from .order import Order
    from .physical_product import PhysicalProduct
    from .supplier import Supplier

    supplier = Supplier("S001", "Test Supplier", "test@example.com")
    product = PhysicalProduct("P001", "Test Product", 100.0, 10, 1.0, supplier)

    # create a student discount strategy
    student_discount = StudentDiscount()

    # create two orders sharing the same discount strategy
    order1 = Order("O001", student_discount)
    order2 = Order("O002", student_discount)

    order1.add_order_line(product, 1)
    order2.add_order_line(product, 1)

    print(f"Order 1 Total: {order1.calculate_total()}")
    print(f"Order 2 Total: {order2.calculate_total()}")
