""" Lab 9 - Validation Tests """

# -----------------------------------
# imports
# -----------------------------------
import unittest

from classes.product_factory import ProductFactory
from classes.supplier import Supplier
from classes.order_line import OrderLine

# -----------------------------------
# tests
# -----------------------------------
class TestValidation(unittest.TestCase):

    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Test Supplier", "test@example.com")

        self.product = ProductFactory.create(
            "physical", "P001", "Desk Lamp", 25.0, 10, self.supplier
        )

    def test_invalid_price(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp", 0, 10, self.supplier
            )

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp", -5, 10, self.supplier
            )

    def test_negative_physical_stock(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp", 25.0, -5, self.supplier
            )

    def test_negative_digital_stock(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "D001", "Photo Editor", 49.90, -5, self.supplier
            )

    def test_zero_stock(self) -> None:
        self.product.update_stock(0)

        self.assertEqual(self.product.to_dict()["stock"], 0)

    def test_invalid_stock_update(self) -> None:
        with self.assertRaises(ValueError):
            self.product.update_stock(-5)

        self.assertEqual(self.product.to_dict()["stock"], 10)

    def test_invalid_order_quantity(self) -> None:
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

        with self.assertRaises(ValueError):
            OrderLine(self.product, -5)

# -----------------------------------
# main
# -----------------------------------
if __name__ == "__main__":
    unittest.main()
