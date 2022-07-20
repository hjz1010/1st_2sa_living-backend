# Generated by Django 4.0.6 on 2022-07-20 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_status_id',
            new_name='order_status',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
