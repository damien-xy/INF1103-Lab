# Lab 8 - UML Class Diagram

```mermaid
classDiagram
    direction TB

    class Product {
        <<abstract>>
        -__product_id: str
        -__name: str
        -__price: float
        -__stock: int
        -__supplier: Supplier
        +update_stock(quantity: int) void
        +display_information() void
        +display_supplier_information() void
        +get_fulfilment_info()* str
        +get_product_id() str
        +get_price() float
        +to_dict() dict
    }

    class Supplier {
        -__supplier_id: str
        -__name: str
        -__contact_email: str
        +display_information() void
        +to_dict() dict
    }

    class Inventory {
        -__products: list~Product~
        +add_product(product: Product) void
        +remove_product(product_id: str) void
        +find_product(product_id: str) Optional~Product~
        +get_products() list~Product~
        +search_product(product_id: str) Optional~Product~
        +display_all() void
        +to_dict_list() list~dict~
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

    class Order {
        -__order_id: str
        -__order_lines: list~OrderLine~
        +add_order_line(product: Product, quantity: int) void
        +calculate_total() float
        +display_order_lines() void
    }

    class OrderLine {
        -__product: Product
        -__quantity: int
        +calculate_subtotal() float
        +display_information() void
    }

    Product <|-- PhysicalProduct
    Product <|-- DigitalProduct

    CanBeShipped <|.. PhysicalProduct

    Inventory "0..1" o-- "0..*" Product
    Supplier "1" -- "0..*" Product : supplies
    Order "1" *-- "0..*" OrderLine
    OrderLine "0..*" -- "1" Product : references
```

### Class Relationships

- **Inheritance:** `PhysicalProduct` and `DigitalProduct` inherit from the abstract `Product` class.
- **Interface Realisation:** `PhysicalProduct` implements `CanBeShipped` to calculate shipping costs.
- **Association:** `Supplier` supplies `Product` objects, while `OrderLine` references a `Product`. Both relationships exist without ownership.
- **Aggregation:** An `Inventory` contains zero or more `Product` objects, which can exist independently of the inventory.
- **Composition:** An `Order` creates and owns its `OrderLine` objects, whose lifecycle is tied to the order.

This design supports the **Single Responsibility Principle (SRP)** by separating responsibilities, the **Open/Closed Principle (OCP)** by allowing new product types without modifying the base `Product` class, and the **Liskov Substitution Principle (LSP)** by allowing subclasses to be used through the common `Product` abstraction.