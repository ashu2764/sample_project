from django.utils.html import format_html
from django.db import models
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.
# category model
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=CloudinaryField('image')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
    return self.title


# post model
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content= HTMLField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=CloudinaryField('image')

def __str__(self):
    return self.cat
