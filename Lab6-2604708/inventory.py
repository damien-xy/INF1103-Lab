""" Lab 6 - Inventory Class for OOP Inventory Management System """

# -----------------------------------
# imports
# -----------------------------------
from product import Product

# -----------------------------------
# classes
# -----------------------------------
class Inventory:
    """ manages a collection of Product objects """

    def __init__(self):
        """ initialises an empty inventory """

        self.__products = []

    def add_product(self, product):
        """ adds a Product object to the inventory """

        self.__products.append(product)

    def search_product(self, product_id):
        """ searches for a product by its ID """

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        """ displays all products in the inventory """

        print("\nCurrent Inventory")
        print("------------------------------------------------")

        for product in self.__products:
            product.display_information()

        print("------------------------------------------------")

    def to_dict_list(self):
        """ returns all products as a list of dictionaries """

        return [product.to_dict() for product in self.__products]

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    inventory = Inventory()

    # create product objects
    product1 = Product("P004", "Monitor", 299.99, 5)
    product2 = Product("P005", "Keyboard", 49.90, 20)

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
