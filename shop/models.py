from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=100, verbose_name="Kategoriya slugi")
    image = models.ImageField(upload_to="category", verbose_name="Kategoriya rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Aktivmi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        db_table = "category"
        ordering = ["-created_at"]


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=203)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        db_table = "product"
        ordering = ["-created_at"]


class PaymentChoice(models.Choices):
    PAYME = "Payme"
    UZCARD = "UzCard"
    HUMO = "Humo"
    CLICK = "Click"
    CASH = "Naqd pul"


class Order(BaseModel):
    first_name = models.CharField(max_length=255, verbose_name="Ism")
    last_name = models.CharField(max_length=255, verbose_name="Familiya")
    phone = models.CharField(max_length=255, verbose_name="Telefon")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    city = models.CharField(max_length=255, verbose_name="Shahar")
    country = models.CharField(max_length=255, verbose_name="Davlat")
    zip_code = models.CharField(max_length=255, verbose_name="Indeks")
    total = models.FloatField(verbose_name="Umumiy summa")
    is_ordered = models.BooleanField(default=False, verbose_name="Buyurtma berildimi")
    is_paid = models.BooleanField(default=False, verbose_name="To'langanmi")
    payment_method = models.CharField(max_length=255, verbose_name="To'lov usuli", choices=PaymentChoice.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")


    def __str__(self):
        return self.first_name


    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        db_table = "order"
        ordering = ["-created_at"]