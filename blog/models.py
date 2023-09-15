from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    #category
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

# Create your models here.