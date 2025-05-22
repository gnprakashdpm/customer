from fastapi import FastAPI, HTTPException
from .models import Customer
from .service import CustomerService

app = FastAPI(title="Customer Service")
service = CustomerService()

@app.get("/customers", response_model=list[Customer])
def list_customers():
    return service.list_customers()

@app.post("/customers", response_model=Customer)
def create_customer(customer: Customer):
    return service.create_customer(customer)

@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):
    try:
        return service.get_customer(customer_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: Customer):
    return service.update_customer(customer_id, customer)

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    service.delete_customer(customer_id)
    return {"status": "deleted"}

