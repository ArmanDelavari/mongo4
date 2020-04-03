from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    # dar khate bala hatman null va blank ro tru mizarim shayd daste bandish kollitar bashe va zir majmue nabashe az khodesh
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)   # allow_uniqye baraye ineke slug dar admin beshe farsi khodesh besaze

    class Meta:
        ordering = ('name',)   # bar hasbe name moratab mikone
        verbose_name = 'category'   # namesh dar panele admin agar moftrad bud
        verbose_name_plural = 'categories'   # namesh agar jam bud

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug])



class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')  # ham masalan gushi a10 betunim tooye ghesmate samusungo  neshun bedim ham tooye ghesmate mobile
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    price = models.IntegerField()   # be khatere zarin bal az integer estefade mikonim az decimal estefade nakonid
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])