# Lab 6 - UML Class Diagram

```mermaid
classDiagram
    direction LR

    class Product {
        -__product_id: str
        -__name: str
        -__price: float
        -__stock: int

        +#95;#95;init#95;#95;(product_id: str, name: str, price: float, stock: int)
        +update_stock(quantity: int) void
        +display_information() void
        +get_product_id() str
        +to_dict() dict
    }

    class Inventory {
        -__products: list

        +#95;#95;init#95;#95;()
        +add_product(product: Product) void
        +search_product(product_id: str) Optional~Product~
        +display_all() void
        +to_dict_list() list
    }

    Inventory "1" o-- "*" Product : contains
```

### Class Relationship

The `Inventory` and `Product` classes have a **one-to-many aggregation relationship**, where one `Inventory` can contain zero or more (`*`) `Product` objects.

This follows the **Single Responsibility Principle (SRP)**, as `Product` manages individual products while `Inventory` manages the collection.