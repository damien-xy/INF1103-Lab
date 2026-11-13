""" Lab 8 - Product Class """

# -----------------------------------
# imports
# -----------------------------------
from abc import ABC, abstractmethod
from supplier import Supplier

# -----------------------------------
# classes
# -----------------------------------
class Product(ABC):
    """ represents and manages an individual product """

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        """ initialises a product with its ID, name, price, stock and supplier """

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    def update_stock(self, quantity):
        """ updates the product's stock quantity """

        if isinstance(quantity, int) and quantity >= 0:
            self.__stock = quantity
        else:
            print("[ERROR] Stock quantity must be a non-negative integer.")

    def display_information(self):
        """ displays the product's information """

        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def display_supplier_information(self) -> None:
        """ displays the product's supplier information """

        self.__supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self):
        """ returns information about how the product is fulfilled """

    def get_product_id(self):
        """ returns the product ID """

        return self.__product_id

    def get_price(self) -> float:
        """ returns the product price """

        return self.__price

    def to_dict(self) -> dict:
        """ returns the product information as a dictionary """

        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # test instantiating the abstract Product class
    try:
        product1 = Product("P004", "Monitor", 299.99, 5, supplier)
    except TypeError as error:
        print(f"[EXPECTED ERROR] {error}")
