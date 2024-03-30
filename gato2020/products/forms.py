from django import forms
from .models import Product, ProductCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'package_weight', 'intensity', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ProductCategory.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        intensity = cleaned_data.get('intensity')

        if category and category.name == 'coffee' and not intensity:
            raise forms.ValidationError("За кафе трябва да определите интензитет.")
