from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus


class ProductTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_products_view(self):
        url = reverse('products:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
