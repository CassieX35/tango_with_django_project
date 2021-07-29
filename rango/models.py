from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) # unique=True is equal to primary key
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # page's catecory 
    title = models.CharField(max_length=128) # page's title
    url = models.URLField() # the url of page
    views = models.IntegerField(default=0) # visiting number of this page

    def __str__(self):
        return self.title
