from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError

class ProductCategory(models.Model):
    name = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    package_weight = models.DecimalField(
        max_digits=4,
        decimal_places=3,
        null=False,
        blank=False
    )

    arabica = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage of arabica content"
    )

    robusta = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage of arabica content"
    )

    image = models.ImageField(
        upload_to='products/images/',
        null=False,
        blank=False
    )

    origin = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Write short description"
    )

    def __str__(self):
        return self.name

    def clean(self):
        if self.category.name == 'кафе на зърна':
            if not self.origin:
                raise ValidationError("Origin is required for coffee products")

            if self.arabica is not None and self.robusta is not None:
                raise ValidationError("Only one of Arabica or Robusta percentage should be provided")

            if self.arabica is not None:
                if self.arabica == 0:
                    self.robusta = 100
                else:
                    self.robusta = 100 - self.arabica

            elif self.robusta is not None:
                if self.robusta == 0:
                    self.arabica = 100
                else:
                    self.arabica = 100 - self.robusta

            else:
                raise ValidationError("Arabica/Robusta percentage is required for coffee products")

        elif self.category.name != 'кафе на зърна':

            if self.origin:
                raise ValidationError("Origin should not be provided for non-coffee products")

            if self.arabica:
                raise ValidationError("Arabica percentage should not be provided for non-coffee products")

            if self.robusta:
                raise ValidationError("Robusta percentage should not be provided for non-coffee products")
