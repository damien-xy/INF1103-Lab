""" Lab 9 - DigitalProduct Class """

# -----------------------------------
# imports
# -----------------------------------
from .product import Product
from .supplier import Supplier

# -----------------------------------
# classes
# -----------------------------------
class DigitalProduct(Product):
    """ represents a digital product with download size """

    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        """ initialises a digital product with its download size and supplier """

        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> None:
        """ displays product information including download size """

        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        """ returns digital product fulfilment information """

        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        """ returns digital product information as a dictionary """

        product_data = super().to_dict()
        product_data["type"] = "digital"
        product_data["download_size"] = self.__download_size

        return product_data

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    product1 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)

    # test displaying digital product information
    product1.display_information()

    # test getting physical product fulfilment information
    print(product1.get_fulfilment_info())

    # test converting digital product to dictionary
    print("\nTesting to_dict():")
    print(product1.to_dict())
