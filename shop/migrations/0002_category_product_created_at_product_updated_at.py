# Generated by Django 4.1.3 on 2022-11-11 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
                ('slug', models.SlugField(max_length=100, verbose_name='Kategoriya slugi')),
                ('image', models.ImageField(upload_to='category', verbose_name='Kategoriya rasmi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktivmi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'db_table': 'category',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]