""" Lab 9 - NoDiscount Class """

# -----------------------------------
# imports
# -----------------------------------
from .discount_strategy import DiscountStrategy

# -----------------------------------
# classes
# -----------------------------------
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total
