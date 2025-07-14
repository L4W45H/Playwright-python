import pytest  # type: ignore
import requests
import asyncio
from playwright.async_api import async_playwright
import nest_asyncio

async def test_get_all_products():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get('https://dummyjson.com/products')
        assert response.status == 200
        data = await response.json()
        print(data)

async def test_add_product():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.post('https://dummyjson.com/products/add', data={"title": "new product"})
        assert response.status == 201
        data = await response.json()
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


nest_asyncio.apply()