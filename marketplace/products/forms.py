from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner', )

    def clean(self):
        print("###############cleaned_data #############")
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        price = cleaned_data.get('price')
        category = cleaned_data.get('category')
        if not (title or price or category):
            raise forms.ValidationError(
                "You must enter either title, price, category or all")
