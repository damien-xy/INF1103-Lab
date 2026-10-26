""" Lab 6 - Product Class for OOP Inventory Management System """

# -----------------------------------
# classes
# -----------------------------------
class Product:
    """ represents and manages an individual product """

    def __init__(self, product_id, name, price, stock):
        """ initialises a product with its ID, name, price and stock """

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

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

    def get_product_id(self):
        """ returns the product ID """

        return self.__product_id

    def to_dict(self):
        """ returns the product information as a dictionary """

        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    product1 = Product("P004", "Monitor", 299.99, 5)

    # test displaying product information
    product1.display_information()

    # test updating stock
    product1.update_stock(10)
    product1.display_information()

    # test invalid stock
    product1.update_stock(-5)
    product1.display_information()

    # test converting product to dictionary
    print("\nTesting to_dict():")
    print(product1.to_dict())
