from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from djangosphinx.models import SphinxSearch
from djangoratings.fields import RatingField
import PIL
from PIL import Image
#from easy_thumbnails.fields import ThumbnailerImageField





class Catalog(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    catalog = models.ForeignKey(Catalog)

    def __unicode__(self):
        return self.name



class Vendor(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField()
    photo = models.ImageField(verbose_name=u'Avatar', upload_to="avatar_pic", blank=True, null=True)
    description = models.TextField(blank=True,
                                   help_text="Describe yourself.")
    user = models.ForeignKey(User, related_name="vendor")
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

class Dashboard(ModelForm):
    class Meta:
        model = Vendor


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    rating = RatingField(range=5) # 5 possible rating values, 1-5
    photo = models.ImageField(verbose_name=u'Photo', upload_to="product_pic", blank=True, null=True)
    categories = models.ManyToManyField(Category)
    catalog = models.ForeignKey(Catalog)
    description = models.TextField(blank=True, help_text="Describe product")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vendor = models.ForeignKey(Vendor)
    search = SphinxSearch(
        index='name',

    )

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name


