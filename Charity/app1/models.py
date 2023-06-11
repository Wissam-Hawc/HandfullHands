from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    phone = models.CharField(max_length=12, default="", unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )


class Donation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_Name = models.CharField(max_length=40)
    last_Name = models.CharField(max_length=40)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=12, default="", unique=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    # payment =


class Program(models.Model):
    program_name = models.CharField(max_length=40)
    program_description = models.CharField(max_length=200)
    program_image = models.ImageField(upload_to='images/')
    budget = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class Content(models.Model):
    PAGE_CHOICES = [
        ('about', 'About'),
        ('contact', 'Contact'),
        ('home-slider1', 'Home Slider 1'),
        ('home-slider2', 'Home Slider 2'),
        ('home-slider3', 'Home Slider 3'),
        ('home-slider4', 'Home Slider 4'),
    ]

    page_name = models.CharField(max_length=40, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    createdAT = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, )
    phone = models.CharField(max_length=12, )
    message = models.CharField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
