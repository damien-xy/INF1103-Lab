# Lab 9 - Predict First Notes

## Section 2

### Section 2.1 - The problem
The business now wants a 5% student discount. Without the Strategy pattern, which class and method must change? After you complete Section 2, answer the same question again for your Strategy version.

| Section | Response |
|---|---|
| **Prediction** | The `Order` class and its `calculate_total()` method must be modified to include the new student discount. |

### Section 2.3 - Use a strategy in Order
Create an order whose lines add up to 250. What will calculate_total() return with BulkDiscount(200, 20)? What if you then call set_discount(PercentageDiscount(10)) on the same order? Write both answers down, then run your code and check.
|  | BulkDiscount(200, 20) | set_discount(PercentageDiscount(10)) |
|---|---|---|
| **Prediction** | 230 | 207 |
