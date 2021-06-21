from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="category", blank=True)


    def add_cart_url(self):
        return reverse("cart:add_cart", args=[self.pk])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse("ecommerceapp:products_by_category", args=[self.slug])

    @property
    def get_update_url(self):
        return reverse("add_cart",kwargs={"product_id": self.id })


    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="Product", blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse("ecommerceapp:ProdCatDetail",args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
