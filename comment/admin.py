from django.contrib import admin
from django.contrib import admin
from .models import Product, Comment, MyUser

admin.site.register(MyUser)
admin.site.register(Product)
admin.site.register(Comment)
