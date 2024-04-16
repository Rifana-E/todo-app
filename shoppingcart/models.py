from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField( max_length=150)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'shoppingcart_category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('category_name', )

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=150)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'shoppingcart_product'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('product_name', )

    def __str__(self):
        return self.product_name


class ShoppedItemList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


    class Meta:
        db_table = 'shoppingcart_shopped_item_list'
        verbose_name = _('shopped_item_list')
        verbose_name_plural = _('shopped_item_lists')
        ordering = ('user', )

    def __str__(self):
        return self.user


