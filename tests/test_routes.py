import unittest
from flask import Flask
from flask_testing import TestCase
from LISTBYNAME2 import create_app, db
from LISTBYNAME2.models import Product

class TestProductRoutes(TestCase):

    def create_app(self):
        app = create_app('testing')  # Ensure you have a testing configuration
        return app

    def setUp(self):
        db.create_all()
        self.product1 = Product(name="Test Product 1", description="This is a test product 1", price=9.99, stock=10)
        self.product2 = Product(name="Test Product 2", description="This is a test product 2", price=19.99, stock=20)
        db.session.add(self.product1)
        db.session.add(self.product2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_list_products_by_name(self):
        # Perform a GET request to list products by name
        response = self.client.get('/products?name=Test Product 1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product 1', response.data)
        self.assertNotIn(b'Test Product 2', response.data)

if __name__ == '__main__':
    unittest.main()
