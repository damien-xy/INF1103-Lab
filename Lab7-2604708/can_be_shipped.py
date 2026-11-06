""" Lab 7 - CanBeShipped Class """

# -----------------------------------
# imports
# -----------------------------------
from abc import ABC, abstractmethod

# -----------------------------------
# interfaces
# -----------------------------------
class CanBeShipped(ABC):
    """ defines the interface for objects that can be shipped """

    @abstractmethod
    def calculate_shipping_cost(self):
        """ calculates and returns the shipping cost """
