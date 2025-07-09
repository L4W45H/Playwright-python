import pytest  # type: ignore
from playwright.sync_api import sync_playwright  # type: ignore
import requests

def test_get_all_products():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get('https://dummyjson.com/products')
        assert response.status == 200
        data = response.json()
        print(data)


def test_add_product():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.post('https://dummyjson.com/products/add', data={"title": "new product"})
        assert response.status == 201
        data = response.json()
        print(data)


def test_update_product():
    response = requests.put(
        'https://dummyjson.com/products/1',
        headers={'Content-Type': 'application/json'},
        json={"title": "iPhone Galaxy +1"}
    )
    data = response.json()
    print(data)

def test_delete_product():
    response = requests.delete('https://dummyjson.com/products/1')
    data = response.json()
    print(data) 