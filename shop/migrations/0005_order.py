# Generated by Django 4.1.3 on 2022-11-11 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_alter_product_options_alter_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=255, verbose_name='Familiya')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon')),
                ('address', models.CharField(max_length=255, verbose_name='Manzil')),
                ('city', models.CharField(max_length=255, verbose_name='Shahar')),
                ('country', models.CharField(max_length=255, verbose_name='Davlat')),
                ('zip_code', models.CharField(max_length=255, verbose_name='Indeks')),
                ('total', models.FloatField(verbose_name='Umumiy summa')),
                ('is_ordered', models.BooleanField(default=False, verbose_name='Buyurtma berildimi')),
                ('is_paid', models.BooleanField(default=False, verbose_name="To'langanmi")),
                ('payment_method', models.CharField(choices=[('Payme', 'Payme'), ('UzCard', 'Uzcard'), ('Humo', 'Humo'), ('Click', 'Click'), ('Naqd pul', 'Cash')], max_length=255, verbose_name="To'lov usuli")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
                'db_table': 'order',
                'ordering': ['-created_at'],
            },
        ),
    ]