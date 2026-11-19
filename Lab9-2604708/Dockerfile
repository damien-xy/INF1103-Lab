FROM python:3.11-slim

WORKDIR /app

COPY product.py physical_product.py digital_product.py can_be_shipped.py inventory.py inventory_manager.py supplier.py order.py order_line.py inventory.json .

CMD ["python", "inventory_manager.py"]