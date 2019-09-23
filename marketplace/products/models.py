from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

# if there are many choices field used, may be it's better to create a file called choices.py
CATEGORY_CHOICES = (
    ('C', 'Casual'),
    ('LS', 'Long Sleeves'),
    ('HS', 'Half Sleeves'),
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
)


class Category(models.Model):
    title = models.CharField(_("title of the category"), max_length=120)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(_("title of the product"), max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.title} - {self.category}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('products:product-detail', args=[str(self.id)])
