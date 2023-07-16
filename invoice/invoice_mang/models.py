from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice_details', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
