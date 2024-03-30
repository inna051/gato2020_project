from django.db import models
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    COFFEE = 'coffee'
    MILK = 'milk'
    COCOA = 'cocoa'
    TEA = 'tea'
    SWEETENERS = 'sweeteners'
    CUPS = 'cups'
    STIRRERS = 'stirrers'
    EXTRAS = 'extras'

    CATEGORY_CHOICES = [
        (COFFEE, 'Кафе'),
        (MILK, 'Мляко'),
        (COCOA, 'Какао'),
        (TEA, 'Чай'),
        (SWEETENERS, 'Подсладители'),
        (CUPS, 'Чаши'),
        (STIRRERS, 'Бъркалки'),
        (EXTRAS, 'Допълнителни'),
    ]

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    package_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    intensity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name
