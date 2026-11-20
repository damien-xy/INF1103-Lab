# Lab 9 - UML Class Diagram

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
        -__discount: DiscountStrategy
        +add_order_line(product: Product, quantity: int) void
        +set_discount(discount: DiscountStrategy) void
        +calculate_total() float
        +display_order_lines() void
    }

    class OrderLine {
        -__product: Product
        -__quantity: int
        +calculate_subtotal() float
        +display_information() void
    }

    class DiscountStrategy {
        <<abstract>>
        +apply(total: float)* float
    }

    class NoDiscount {
        +apply(total: float) float
    }

    class PercentageDiscount {
        +percentage: float
        +apply(total: float) float
    }

    class BulkDiscount {
        +threshold: float
        +amount: float
        +apply(total: float) float
    }

    class StudentDiscount {
        +apply(total: float) float
    }

    class ProductFactory {
        +create(product_type: str, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float, download_size: float) Product$
    }

    %% Inheritance
    Product <|-- PhysicalProduct
    Product <|-- DigitalProduct
    DiscountStrategy <|-- NoDiscount
    DiscountStrategy <|-- PercentageDiscount
    DiscountStrategy <|-- BulkDiscount
    DiscountStrategy <|-- StudentDiscount

    %% Realisation
    CanBeShipped <|.. PhysicalProduct

    %% Association
    Supplier "1" -- "0..*" Product : supplies
    OrderLine "0..*" -- "1" Product : references
    Order "0..*" --> "1" DiscountStrategy : uses

    %% Aggregation
    Inventory "0..1" o-- "0..*" Product

    %% Composition
    Order "1" *-- "0..*" OrderLine

    %% Dependency
    ProductFactory ..> Product : «creates»
```

### Class Relationships

- **Inheritance:** `PhysicalProduct` and `DigitalProduct` inherit from the abstract `Product` class. `NoDiscount`, `PercentageDiscount`, `BulkDiscount` and `StudentDiscount` inherit from the abstract `DiscountStrategy` class.
- **Interface Realisation:** `PhysicalProduct` implements `CanBeShipped` to calculate shipping costs.
- **Association:** `Supplier` supplies `Product` objects, `OrderLine` references a `Product`, and `Order` uses a `DiscountStrategy`. These relationships exist without exclusive ownership.
- **Aggregation:** An `Inventory` contains zero or more `Product` objects, which can exist independently of the inventory.
- **Composition:** An `Order` creates and owns its `OrderLine` objects, whose lifecycle is tied to the order.
- **Dependency:** `ProductFactory` creates `Product` objects without storing or owning them.

This design supports the **Single Responsibility Principle (SRP)** by separating responsibilities, the **Open/Closed Principle (OCP)** by allowing new discount strategies without modifying `Order`, and the **Liskov Substitution Principle (LSP)** by allowing subclasses to be used through their common abstractions.

Although `ProductFactory` still requires modification when new product types are introduced, it centralises product creation and reduces coupling.

### AI Use Review (Lab 8)

- **Accepted:** I accepted the suggestion to represent the relationship between `Supplier` and `Product` as association because neither object owns the other, and both can exist independently.
- **Changed:** I updated the aggregation multiplicity between `Inventory` and `Product` from `1` to `0..1` at the Inventory end after reviewing the lab sheet, as a Product can exist without belonging to an Inventory.
