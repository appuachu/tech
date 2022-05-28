from django.db import models

# Create your models here.
class gal(models.Model):
    image=models.ImageField(upload_to='static')
    disc=models.TextField(max_length=200)
    discc=models.TextField(max_length=200)
class contact(models.Model):
    def __str__(self):
        return self.Email
    location=models.TextField(max_length=200)
    time=models.IntegerField()
    Phone=models.TextField(max_length=10)
    Email=models.TextField(max_length=400)

class event(models.Model):
    def __str__(self):
        return self.event_name
    img=models.ImageField(upload_to="static")
    date=models.IntegerField()
    month=models.TextField(max_length=100)
    event_name=models.TextField(max_length=100)
    discc=models.TextField(max_length=3000)
    event_contact=models.IntegerField(max_length=10)

class font(models.Model):
    def __str__(self):
        return self.font
    font=models.TextField()
    size=models.IntegerField()
    color=models.TextField()