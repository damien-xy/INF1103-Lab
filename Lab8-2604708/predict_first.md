# Lab 8 - Predict First Notes

## Section 2.2 - Associate Supplier with Product
Before you run this test, write down what you expect to happen if you delete your supplier variable (del supplier) after creating the products. Can each Product still display its supplier information? Run it and check. If your prediction did not match, note why.

| Section | Response |
|---|---|
| **Prediction** | I predict that both products will still be able to display their supplier information because they were created before the `supplier` variable was deleted. Each product already stores a reference to the Supplier object, so deleting the original variable should not affect their access to it. |
| **Actual Result** | Both the physical and digital products were still able to display their supplier information after the `supplier` variable was deleted. The output matched my prediction. |

## Section 3.2 - Add and remove products
Before step 3, write down whether you expect the Product to still work after it is removed from Inventory A, and why. Then check. 

| Section | Response |
|---|---|
| **Prediction** | I predict that the Product object will no longer work after being removed from Inventory A because it has been removed from the inventory's collection of products. |
| **Actual Result** | The Product object could still display its information after being removed from Inventory A and was successfully added to Inventory B. This differed from my prediction because removing a product from an inventory only removes its reference from the inventory's collection, not the actual object. The Product object still exists because `product1` holds a reference to it. |