# Generated by Django 3.1.2 on 2020-10-28 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20201028_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bidremaining',
            field=models.CharField(default=models.CharField(choices=[('500', 'R500'), ('1000', 'R1000'), ('2000', 'R2000'), ('5000', 'R5000')], max_length=200, null=True), max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='CustomerBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('declined', 'Declined')], max_length=200, null=True)),
                ('bider', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.bids')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.customer')),
            ],
        ),
    ]
