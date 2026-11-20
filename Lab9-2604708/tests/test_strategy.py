""" Lab 9 - Strategy Pattern Tests """

# -----------------------------------
# imports
# -----------------------------------
import unittest

from classes.order import Order
from classes.supplier import Supplier
from classes.product_factory import ProductFactory
from classes.no_discount import NoDiscount
from classes.percentage_discount import PercentageDiscount
from classes.bulk_discount import BulkDiscount
from classes.student_discount import StudentDiscount

# -----------------------------------
# tests
# -----------------------------------
class TestStrategy(unittest.TestCase):

    def setUp(self) -> None:
        supplier = Supplier("S001", "Test Supplier", "test@example.com")

        self.product = ProductFactory.create(
            "physical", "P001", "Test Product", 125.0, 10, supplier
        )

    def test_no_discount(self) -> None:
        self.assertAlmostEqual(NoDiscount().apply(250), 250.0)

    def test_percentage_discount(self) -> None:
        self.assertAlmostEqual(PercentageDiscount(10).apply(250), 225.0)

    def test_bulk_discount(self) -> None:
        discount = BulkDiscount(200, 20)

        self.assertAlmostEqual(discount.apply(150), 150.0)
        self.assertAlmostEqual(discount.apply(200), 180.0)
        self.assertAlmostEqual(discount.apply(250), 230.0)

    def test_student_discount(self) -> None:
        order = Order("O001", StudentDiscount())
        order.add_order_line(self.product, 2)

        self.assertAlmostEqual(order.calculate_total(), 237.5)

    def test_default_discount(self) -> None:
        order = Order("O001")
        order.add_order_line(self.product, 2)

        self.assertAlmostEqual(order.calculate_total(), 250.0)

    def test_set_discount(self) -> None:
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(self.product, 2)

        self.assertAlmostEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))

        self.assertAlmostEqual(order.calculate_total(), 225.0)

# -----------------------------------
# main
# -----------------------------------
if __name__ == "__main__":
    unittest.main()
