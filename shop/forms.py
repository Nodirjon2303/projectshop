from django import forms
from .models import Category, Product


class ProductForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    stock = forms.IntegerField()
    image_url = forms.URLField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'stock', 'image_url']

    def clean_image_url(self):
        image = self.cleaned_data['image_url'].split('.')[-1]
        if image not in ['jpg', 'JPG', 'png', 'PNG']:
            raise forms.ValidationError("Rasm formati noto'g'ri")
        return self.cleaned_data['image_url']

    def clean_stock(self):
        if self.cleaned_data['stock'] < 0:
            raise forms.ValidationError("Mahsulot soni manfiy bo'la olmaydi")
        return self.cleaned_data['stock']
