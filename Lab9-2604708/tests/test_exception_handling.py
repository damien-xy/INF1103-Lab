""" Lab 9 - Exception Handling Tests """

# -----------------------------------
# imports
# -----------------------------------
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from classes.inventory import Inventory
from classes.supplier import Supplier
from inventory_manager import get_positive_float, load_products

# -----------------------------------
# tests
# -----------------------------------
class TestExceptionHandling(unittest.TestCase):

    def setUp(self) -> None:
        self.inventory = Inventory()
        self.supplier = Supplier("S001", "Test Supplier", "test@example.com")

    def test_invalid_user_input(self) -> None:
        output = StringIO()

        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            with redirect_stdout(output):
                result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)
        self.assertIn("Please enter a valid number, e.g. 12.50", output.getvalue())
        self.assertIn("Please enter a number greater than zero.", output.getvalue())

    def test_missing_products_file(self) -> None:
        output = StringIO()

        with TemporaryDirectory() as directory:
            path = str(Path(directory) / "missing.csv")

            with redirect_stdout(output):
                load_products(path, self.inventory, self.supplier)

            self.assertIn(f"Products file not found: {path}", output.getvalue())

        self.assertIn("Load attempt finished.", output.getvalue())
        self.assertEqual(len(self.inventory.get_products()), 0)

    def test_load_products_with_invalid_rows(self) -> None:
        output = StringIO()
        path = Path(__file__).resolve().parent.parent / "products.csv"

        with redirect_stdout(output):
            load_products(str(path), self.inventory, self.supplier)

        self.assertEqual(len(self.inventory.get_products()), 3)
        self.assertIn("Unknown product type: service", output.getvalue())
        self.assertIn("could not convert string to float: 'abc'", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

# -----------------------------------
# main
# -----------------------------------
if __name__ == "__main__":
    unittest.main()
