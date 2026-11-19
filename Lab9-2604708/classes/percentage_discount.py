""" Lab 9 - PercentageDiscount Class """

# -----------------------------------
# imports
# -----------------------------------
from .discount_strategy import DiscountStrategy

# -----------------------------------
# classes
# -----------------------------------
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)
