# Customer Microservice

This repository contains a simple Spring Boot application that provides a basic
in-memory customer service. The project exposes REST endpoints to create,
retrieve, update and delete customer records.

## Build and Run

The service uses Maven. From the `customer-service` directory run:

```bash
mvn spring-boot:run
```

The application will start on port `8080`.

## API Endpoints

- `GET /customers` — list all customers
- `POST /customers` — create a new customer
- `GET /customers/{id}` — retrieve a customer by ID
- `PUT /customers/{id}` — update an existing customer
- `DELETE /customers/{id}` — delete a customer
