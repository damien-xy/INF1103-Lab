""" Lab 9 - ProductFactory Class """

# -----------------------------------
# imports
# -----------------------------------
from .product import Product
from .physical_product import PhysicalProduct
from .digital_product import DigitalProduct
from .supplier import Supplier

# -----------------------------------
# classes
# -----------------------------------
class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str,
               price: float, stock: int, supplier: Supplier,
               weight: float = 0.0, download_size: float = 0.0) -> Product:

        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, weight, supplier)

        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, download_size, supplier)

        else:
            raise ValueError(f"Unknown product type: {product_type}")

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    supplier = Supplier("S001", "Test Supplier", "test@example.com")

    # test physical product creation
    physical_product = ProductFactory.create(
        "physical", "P001", "Desk Lamp", 25.0, 10, supplier, weight=1.5
    )
    print(f"Physical Product: {type(physical_product).__name__}")

    # test digital product creation
    digital_product = ProductFactory.create(
        "digital", "D001", "Photo Editor", 49.90, 100, supplier, download_size=50.0
    )
    print(f"Digital Product: {type(digital_product).__name__}")

    # test an unknown product type
    try:
        ProductFactory.create(
            "service", "S001", "Installation", 30.0, 5, supplier
        )
    except ValueError as e:
        print(f"Error: {e}")
