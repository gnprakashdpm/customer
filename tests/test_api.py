from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_customer():
    response = client.post('/customers', json={'id': 0, 'name': 'John', 'email': 'john@example.com'})
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    cust_id = data['id']

    response = client.get(f'/customers/{cust_id}')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'John'
    assert data['email'] == 'john@example.com'


def test_list_customers():
    client.post('/customers', json={'id': 0, 'name': 'Alice', 'email': 'alice@example.com'})
    response = client.get('/customers')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_customer():
    response = client.post('/customers', json={'id': 0, 'name': 'Bob', 'email': 'bob@example.com'})
    cust_id = response.json()['id']
    response = client.delete(f'/customers/{cust_id}')
    assert response.status_code == 200
    response = client.get(f'/customers/{cust_id}')
    assert response.status_code == 404

