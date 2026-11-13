
# Lab 8 - Polymorphism Notes (Section 7)

## Section 7.3 - Connect Polymorphism to LSP
Review your `show_product_details(product: Product)` function from the previous section. It should work with both product types without modification. Explain how this demonstrates polymorphism and how LSP supports the design.

**Answer:**

The `show_product_details()` function demonstrates polymorphism because both `PhysicalProduct` and `DigitalProduct` use their own implementations of `get_fulfilment_info()` through the common `Product` abstraction. LSP supports this design by ensuring that both subclasses can be used in place of `Product` without breaking the function's expected behaviour.
