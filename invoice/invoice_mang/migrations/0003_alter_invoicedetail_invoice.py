# Generated by Django 4.2.3 on 2023-07-14 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_mang', '0002_rename_invoicedetails_invoicedetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_details', to='invoice_mang.invoice'),
        ),
    ]