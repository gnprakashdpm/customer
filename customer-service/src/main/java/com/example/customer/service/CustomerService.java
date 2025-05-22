package com.example.customer.service;

import com.example.customer.model.Customer;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class CustomerService {
    private final Map<Long, Customer> customers = new HashMap<>();
    private final AtomicLong counter = new AtomicLong();

    public List<Customer> findAll() {
        return new ArrayList<>(customers.values());
    }

    public Customer create(Customer customer) {
        long id = counter.incrementAndGet();
        customer.setId(id);
        customers.put(id, customer);
        return customer;
    }

    public Optional<Customer> findById(Long id) {
        return Optional.ofNullable(customers.get(id));
    }

    public Optional<Customer> update(Long id, Customer updated) {
        Customer existing = customers.get(id);
        if (existing == null) {
            return Optional.empty();
        }
        existing.setName(updated.getName());
        existing.setEmail(updated.getEmail());
        return Optional.of(existing);
    }

    public boolean delete(Long id) {
        return customers.remove(id) != null;
    }
}
