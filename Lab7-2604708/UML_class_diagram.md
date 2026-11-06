# Lab 7 - UML Class Diagram

```mermaid
classDiagram
    direction TB

    class Product {
        <<abstract>>
        -__product_id: str
        -__name: str
        -__price: float
        -__stock: int
        +update_stock(quantity: int) void
        +display_information() void
        +get_fulfilment_info()* str
        +get_product_id() str
        +to_dict() dict
    }

    class Inventory {
        -__products: list~Product~
        +add_product(product: Product) void
        +search_product(product_id: str) Optional~Product~
        +display_all() void
        +to_dict_list() list
    }

    class PhysicalProduct {
        -__weight: float
        +display_information() void
        +get_fulfilment_info() str
        +calculate_shipping_cost() float
        +to_dict() dict
    }

    class DigitalProduct {
        -__download_size: float
        +display_information() void
        +get_fulfilment_info() str
        +to_dict() dict
    }

    class CanBeShipped {
        <<interface>>
        +calculate_shipping_cost()* float
    }

    Product <|-- PhysicalProduct
    Product <|-- DigitalProduct

    CanBeShipped <|.. PhysicalProduct

    Inventory "1" o-- "0..*" Product
```

### Class Relationship

- **Inheritance:** `PhysicalProduct` and `DigitalProduct` inherit from the abstract `Product` class.
- **Interface Realisation:** `PhysicalProduct` implements `CanBeShipped` to calculate shipping costs.
- **Aggregation:** One `Inventory` contains zero or more `Product` objects.

This design supports **Single Responsibility Principle (SRP)** by separating responsibilities and **Open Close Principle (OCP)** by allowing new product types without modifying the base `Product` class.