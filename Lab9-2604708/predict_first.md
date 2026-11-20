# Lab 9 - Predict First Notes

## Section 2 - Implement the Strategy pattern: order discounts

### Section 2.1 - The problem
The business now wants a 5% student discount. Without the Strategy pattern, which class and method must change? After you complete Section 2, answer the same question again for your Strategy version.

|  | Response |
|---|---|
| **Prediction** | The `Order` class and its `calculate_total()` method must be modified to include the new student discount. |
| **After implementing Strategy** | Only a new `StudentDiscount` class was needed, inheriting from `DiscountStrategy` and implementing `apply()`. The `Order` class and its `calculate_total()` method did not need to be modified, following the Open/Closed Principle (OCP). |

### Section 2.3 - Use a strategy in Order
Create an order whose lines add up to 250. What will `calculate_total()` return with `BulkDiscount(200, 20)`? What if you then call `set_discount(PercentageDiscount(10))` on the same order? Write both answers down, then run your code and check.
|  | `BulkDiscount(200, 20)` | `set_discount(PercentageDiscount(10))` |
|---|---|---|
| **Prediction** | 230 | 207 |
| **Actual Result** | 230 | 225 |

**Notes:**
- My BulkDiscount prediction was correct, but the PercentageDiscount prediction was incorrect because `set_discount()` replaces the previous discount strategy rather than applying an additional discount. The 10% discount is calculated from the original total of 250, resulting in 225 instead of 207.

### Section 2.4 - Extend without modifying
Look back at Lab 8. Which relationship best describes `Order` and `DiscountStrategy`: association, aggregation or composition? Hint: is a discount part of an order, or something the order uses? Could two orders share the same `PercentageDiscount` object? Write your answer and a multiplicity for each end, then check it against your code.

|  | Response |
|---|---|
| **Prediction** | Association. An `Order` uses one `DiscountStrategy` at a time, while a `DiscountStrategy` can be shared by multiple orders. The multiplicities are 1 at the `DiscountStrategy` end and 0..* at the `Order` end. |
| **Actual Result** | Same as prediction. Both orders successfully shared the same `StudentDiscount` object, confirming the association relationship. |

## Section 3 - Implement the Factory pattern: creating products

### Section 3.2 - Create a ProductFactory
WWhat happens if you call `ProductFactory.create("service", ...)`? Which line raises the exception, and what happens to your program if nothing catches it? Run it and check.

|  | Response |
|---|---|
| **Prediction** | Since `"service"` does not match `"physical"` or `"digital"`, the `else` block raises a `ValueError` at `raise ValueError(f"Unknown product type: {product_type}")`. If the exception is not caught, the program terminates with an error. |
| **Actual Result** | Same as prediction. Line 27 raised a `ValueError` with the message `Unknown product type: service`, and the program terminated with a traceback because the exception was not caught. |

### Section 3.3 - Who knows about what?
Suppose a new BundleProduct type is added. How many places in your code would need to change before you added the factory, and how many after? Count them, then explain why the factory still breaks OCP and why that is acceptable here.

|  | Before | After |
|---|---|---|
| **Prediction (only considering changes to product creation logic)** | 2 places: `add_product()` and `load_inventory()` | 1 place: `ProductFactory.create()` |

**Explanation:** 
- The factory still breaks OCP because its `create()` method must be modified whenever a new product type is added.
- This is acceptable because product creation is centralised in one place, reducing coupling and improving maintainability.

**Actual Result:**
- Same as prediction. Product creation logic previously existed in 2 functions but is now centralised in 1 method, `ProductFactory.create()`.

## Section 4 - Add validation
Think back to the Lab 8 LSP discussion. If Product validates that stock cannot go negative, should DigitalProduct be allowed to skip or change that rule? Why? 

|  | Response |
|---|---|
| **Prediction** | No. `DigitalProduct` should follow the same stock validation rules as `Product`. Allowing negative stock would violate LSP, as subclasses should maintain the expected behaviour of their parent class. |
| **Actual Result** |  |
