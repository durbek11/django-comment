from audioop import add
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1, null=True, blank=True)
    img = models.ImageField(upload_to="images/")
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(f"id:{self.pk} score:{self.score} title:{self.title}")

class Comment(models.Model):
    post = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    authour = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    rate_product = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    active = models.BooleanField(default=True)

class Contact(models.Model):
    TAKLIF = "Taklif"
    SHIKOYAT = "Shikoyat"
    CONTACT_CHOICES = [
        (TAKLIF, "Taklif"),
        (SHIKOYAT, "Shikoyat")
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    choices = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=TAKLIF)
    mobile = models.IntegerField(default=9989)
    message = models.TextField(max_length=700)
    date = models.DateTimeField(auto_now=add)
    def __str__(self):
        return self.choices