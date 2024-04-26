from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES= (
        ('d','Draft'),
        ('p','Publish'),
        
    )
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True) #برای زمانی که مقاله کی ایجاد شده چه منتشر شود چه نشود
    updated = models.DateTimeField(auto_now = True) #این برای زمانی هستش که نمایش می دهد کی ملاقه عوض شده
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)