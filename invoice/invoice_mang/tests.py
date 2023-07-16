from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'invoice_number': 'INV-001',
            'customer_name': 'John Doe',
            'total_amount': '100.00',
            'invoice_details': [
                {
                    'product_name': 'Product A',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'total_price': '20.00',
                },
                {
                    'product_name': 'Product B',
                    'quantity': 3,
                    'unit_price': '5.00',
                    'total_price': '15.00',
                },
            ],
        }

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        print(response.data,"# Add this line to print the response data")  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invoice_without_invoice_details(self):
        invoice_data = {
            'invoice_number': 'INV-002',
            'customer_name': 'Jane Smith',
            'total_amount': '50.00',
            'invoice_details': [],  # Provide an empty list
        }
        response = self.client.post('/api/invoices/', invoice_data, format='json')
        print(response.data)  # Add this line to print the response data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_invoices(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
