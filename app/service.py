from typing import Dict, List
from .models import Customer

class CustomerService:
    def __init__(self) -> None:
        self.customers: Dict[int, Customer] = {}
        self.next_id = 1

    def list_customers(self) -> List[Customer]:
        return list(self.customers.values())

    def create_customer(self, customer: Customer) -> Customer:
        customer.id = self.next_id
        self.customers[self.next_id] = customer
        self.next_id += 1
        return customer

    def get_customer(self, customer_id: int) -> Customer:
        return self.customers[customer_id]

    def update_customer(self, customer_id: int, customer: Customer) -> Customer:
        customer.id = customer_id
        self.customers[customer_id] = customer
        return customer

    def delete_customer(self, customer_id: int) -> None:
        if customer_id in self.customers:
            del self.customers[customer_id]

