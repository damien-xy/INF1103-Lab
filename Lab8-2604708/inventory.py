""" Lab 8 - Inventory Class """

# -----------------------------------
# imports
# -----------------------------------
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from product import Product

# -----------------------------------
# classes
# -----------------------------------
class Inventory:
    """ manages a collection of Product objects """

    def __init__(self) -> None:
        """ initialises an empty inventory """

        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """ adds a Product object to the inventory """

        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        """ removes a Product reference from the inventory """

        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                return

    def find_product(self, product_id: str) -> Product | None:
        """ finds a product by its ID """

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def get_products(self) -> list[Product]:
        """ returns a list of products in the inventory """

        return self.__products.copy()

    def search_product(self, product_id: str) -> Product | None:
        """ searches for a product using find_product() """

        return self.find_product(product_id)

    def display_all(self) -> None:
        """ displays all products in the inventory """

        print("\nCurrent Inventory")
        print("------------------------------------------------")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")

    def to_dict_list(self) -> list[dict]:
        """ returns all products as a list of dictionaries """

        return [product.to_dict() for product in self.__products]

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    inventory = Inventory()

    # create supplier
    supplier = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # create physical and digital product objects
    product1 = PhysicalProduct("P004", "Monitor", 299.99, 5, 3.5, supplier)
    product2 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5, supplier)

    # test adding products
    inventory.add_product(product1)
    inventory.add_product(product2)

    # test displaying all products
    inventory.display_all()

    # test searching for an existing product
    print("\nSearching for P004:")
    product = inventory.search_product("P004")

    if product is not None:
        product.display_information()
    else:
        print("Product not found.")

    # test searching for a non-existing product
    print("\nSearching for P999:")
    product = inventory.search_product("P999")

    if product is not None:
        product.display_information()
    else:
        print("Product not found.")

    # test converting inventory to list of dictionaries
    print("\nTesting to_dict_list():")
    print(inventory.to_dict_list())
