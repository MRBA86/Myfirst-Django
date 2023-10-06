from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)


    class Meta:
        ordering = ['-created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return "{} - {} ".format(self.title,self.id)
    

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
    
    def __str__(self):
        return self.name

# Create your models here.
