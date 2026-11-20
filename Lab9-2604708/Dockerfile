
FROM python:3.11-slim

WORKDIR /app

COPY classes/ ./classes/
COPY tests/ ./tests/
COPY inventory_manager.py inventory.json products.csv .

CMD ["python", "inventory_manager.py"]