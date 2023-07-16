from django.urls import path
from .views import InvoiceListView

app_name = 'invoice_mang'

urlpatterns = [
    path('api/invoices/', InvoiceListView.as_view(), name='invoice-list'),
]
