# Lab 8 - Predict First Notes

## Section 2.2 - Associate Supplier with Product
Before you run this test, write down what you expect to happen if you delete your supplier variable (del supplier) after creating the products. Can each Product still display its supplier information? Run it and check. If your prediction did not match, note why.

| Section | Response |
|---|---|
| **Prediction** | I predict that both products will still be able to display their supplier information because they were created before the `supplier` variable was deleted. Each product already stores a reference to the Supplier object, so deleting the original variable should not affect their access to it. |
| **Actual Result** |  |
