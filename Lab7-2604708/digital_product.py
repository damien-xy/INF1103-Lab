""" Lab 7 - Digital Product Class """

# -----------------------------------
# imports
# -----------------------------------
from product import Product

# -----------------------------------
# classes
# -----------------------------------
class DigitalProduct(Product):
    """ represents a digital product with download size """

    def __init__(self, product_id, name, price, stock, download_size):
        """ initialises a digital product with its download size """

        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        """ displays product information including download size """

        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    product1 = DigitalProduct("P005", "Antivirus Software", 49.90, 20, 250.5)

    # test displaying digital product information
    product1.display_information()
