from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder
from django.contrib.auth.models import User

class VendorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_create_vendor(self):
        url = reverse('vendor-list-create')
        data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact details',
            'address': 'Test Address',
            'vendor_code': '1234'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)
        self.assertEqual(Vendor.objects.get().name, 'Test Vendor')

class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='Contact details', address='Test Address', vendor_code='1234')

    def test_create_purchase_order(self):
        url = reverse('purchaseorder-list-create')
        data = {
            'po_number': 'PO123',
            'vendor': self.vendor.id,
            'order_date': '2024-04-30T10:00:00Z',
            'delivery_date': '2024-05-10T10:00:00Z',
            'items': ['item1', 'item2'],
            'quantity': 10,
            'status': 'pending',
            'issue_date': '2024-04-30T10:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(PurchaseOrder.objects.get().po_number, 'PO123')

    def test_retrieve_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            order_date='2024-04-30T10:00:00Z',
            delivery_date='2024-05-10T10:00:00Z',
            items=['item1', 'item2'],
            quantity=10,
            status='pending',
            issue_date='2024-04-30T10:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['po_number'], 'PO123')

    def test_update_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            order_date='2024-04-30T10:00:00Z',
            delivery_date='2024-05-10T10:00:00Z',
            items=['item1', 'item2'],
            quantity=10,
            status='pending',
            issue_date='2024-04-30T10:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        data = {'status': 'completed'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PurchaseOrder.objects.get(id=purchase_order.id).status, 'completed')

    def test_delete_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            order_date='2024-04-30T10:00:00Z',
            delivery_date='2024-05-10T10:00:00Z',
            items=['item1', 'item2'],
            quantity=10,
            status='pending',
            issue_date='2024-04-30T10:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
