""" Lab 9 - Factory Pattern Tests """

# -----------------------------------
# imports
# -----------------------------------
import unittest

from classes.product_factory import ProductFactory
from classes.physical_product import PhysicalProduct
from classes.digital_product import DigitalProduct
from classes.supplier import Supplier

# -----------------------------------
# tests
# -----------------------------------
class TestFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Test Supplier", "test@example.com")

    def test_create_physical_product(self) -> None:
        product = ProductFactory.create(
            "physical", "P001", "Desk Lamp", 25.0, 10,
            self.supplier, weight=1.5
        )

        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self) -> None:
        product = ProductFactory.create(
            "digital", "D001", "Photo Editor", 49.90, 100,
            self.supplier, download_size=50.0
        )

        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create(
                "service", "S001", "Installation", 30.0, 5,
                self.supplier
            )

# -----------------------------------
# main
# -----------------------------------
if __name__ == "__main__":
    unittest.main()
