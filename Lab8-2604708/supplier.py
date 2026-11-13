""" Lab 8 - Supplier Class """

# -----------------------------------
# classes
# -----------------------------------
class Supplier:
    """ represents a supplier of products """

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        """ initialises a supplier with its details """

        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        """ displays the supplier's information """

        print(
            f"Supplier ID: {self.__supplier_id} | "
            f"Name: {self.__name} | "
            f"Email: {self.__contact_email}"
        )

# -----------------------------------
# testing
# -----------------------------------
if __name__ == "__main__":
    supplier1 = Supplier("S001", "Tech Supplies Pte Ltd", "contact@techsupplies.com")

    # test displaying supplier information
    supplier1.display_information()
