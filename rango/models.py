from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):

    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True) # unique=True is equal to primary key
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE) # page's catecory 
    title = models.CharField(max_length=TITLE_MAX_LENGTH) # page's title
    url = models.URLField() # the url of page
    views = models.IntegerField(default=0) # visiting number of this page

    def __str__(self):
        return self.title
