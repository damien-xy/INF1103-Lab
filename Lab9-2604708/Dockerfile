FROM python:3.11-slim

WORKDIR /app

COPY classes/ ./classes/
COPY inventory_manager.py inventory.json .

CMD ["python", "inventory_manager.py"]