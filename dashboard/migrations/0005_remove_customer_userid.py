# Generated by Django 3.1.2 on 2020-10-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_customer_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='userId',
        ),
    ]
