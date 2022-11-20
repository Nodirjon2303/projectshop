from django.contrib import admin
from django.utils import timezone
from datetime import datetime

from django.utils.html import format_html

from .models import Product, Category, Order, OrderProduct


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'image_tag']
    list_display_links = ('name',)
    list_filter = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    list_per_page = 10
    search_help_text = "Qidirayotgan mahsulotingiz nomini kiriting"
    save_as = True

    def image_tag(self, obj):
        return format_html('<img style="width:40%; height:40%" src="{}" />'.format(obj.image_url))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'image_tag']
    list_display_links = ('name',)
    list_filter = ('created_at',)
    list_editable = ('is_active',)
    search_fields = ('name', 'slug')
    readonly_fields = ('image_tag',)
    list_per_page = 10
    search_help_text = "Qidirayotgan mahsulotingiz nomini yoki slugini kiriting"

    def image_tag(self, obj):
        return format_html('<img style="width:40%; height:40%" src="{}" />'.format(obj.image.url))


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'country', 'payment_method', 'created_at']
    list_display_links = ('first_name',)
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'phone', 'city', 'country')
    list_per_page = 10
    search_help_text = "Qidirayotgan buyurtmangiz nomini yoki telefon raqamingizni kiriting"


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'total_price']
    search_help_text = 'mahsulot nomi bo\'yicha izlang'
    search_fields = ['product__name']
    readonly_fields = ('product_price', 'total_price', 'price')

    def total_price(self, obj):
        if obj.pk:
            try:
                return obj.quantity * obj.price
            except Exception as e:
                return 'x'

        else:
            return '-'

    def product_price(self, obj):
        return obj.product.price
