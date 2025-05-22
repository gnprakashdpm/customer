# Customer Microservice

This repository contains a minimal FastAPI microservice that manages e-commerce customers. The service supports basic CRUD operations and keeps data in memory.

## Endpoints

- `GET /customers` - List all customers
- `POST /customers` - Create a new customer
- `GET /customers/{customer_id}` - Retrieve a customer by ID
- `PUT /customers/{customer_id}` - Update an existing customer
- `DELETE /customers/{customer_id}` - Delete a customer

## Development

Install dependencies (if not already installed) and run tests:

```bash
pip install fastapi uvicorn pytest
pytest
```

To start the service locally:

```bash
uvicorn app.main:app --reload
```

