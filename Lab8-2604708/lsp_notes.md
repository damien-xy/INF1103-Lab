# Lab 8 - LSP Notes (Section 6)

## Q1
Identify one expectation that Product establishes and explain how both subclasses preserve it.

**Answer:**

The `Product` class establishes that `update_stock()` accepts a non-negative integer to update a product's stock quantity. Both `PhysicalProduct` and `DigitalProduct` inherit this method without overriding it, preserving the same expected behaviour.

## Q2 - LSP Diagonsis
A teammate proposes this DigitalProduct method. The program runs until Inventory calls update_stock() on a digital product.
```
class DigitalProduct(Product): 
    def update_stock(self, quantity: int) -> None: 
        raise NotImplementedError("Digital products have no stock") 
```
Does this violate LSP? What would you change: the subclass, the parent class (Product), or the inheritance relationship? Write 2–3 sentences explaining your choice.

**Answer:**

Yes, this violates LSP because `DigitalProduct` would raise an exception when `update_stock()` is called, instead of behaving as expected of a `Product`. I would change the `DigitalProduct` subclass by removing the overridden method and allowing it to inherit `update_stock()` from the parent class. This ensures that both physical and digital products can update their stock without breaking the expected behaviour.