from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    phone = models.CharField(max_length=12, default="", unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class GuestUser(models.Model):
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Donation(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    guest_user = models.ForeignKey(GuestUser, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, default="")
    amount = models.IntegerField()
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    stripeid = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Donation ID: {self.id}, Amount: {self.amount}"


class Program(models.Model):
    program_name = models.CharField(max_length=40)
    program_description = models.CharField(max_length=200)
    program_image = models.ImageField(upload_to='images/')
    budget = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    raised = models.IntegerField(default=0)
    program_challenge = models.CharField(max_length=2000, default='Default Value')
    program_objective = models.CharField(max_length=2000, default='Default Value')
    program_plan = models.CharField(max_length=2000, default='Default Value')

    def __str__(self):
        return self.program_name


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
    image = models.ImageField(upload_to='images/', blank=True)
    createdAT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_name


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
