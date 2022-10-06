from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=500,blank=False)
    author = models.CharField(max_length=100,blank=False)
    synopsis = models.TextField(blank=True)
    
    def __str__(self):
        return "{} by {}".format(self.title,self.author)
    
class BookReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=500,blank=False)
    stars = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(4)])
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)
    
    def __str__(self):
        return "Review of {} by {}".format(self.book.title,self.user.username)