""" Lab 9 - DiscountStrategy Class """

# -----------------------------------
# imports
# -----------------------------------
from abc import ABC, abstractmethod

# -----------------------------------
# classes
# -----------------------------------
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
