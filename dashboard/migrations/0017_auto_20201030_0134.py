# Generated by Django 3.1.2 on 2020-10-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_buybid_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='remainingbid',
            field=models.IntegerField(default=models.CharField(choices=[('500', 'R500'), ('1000', 'R1000'), ('2000', 'R2000'), ('5000', 'R5000')], max_length=200, null=True)),
        ),
    ]
