from django.contrib import admin
from .models import Category
from .models import Customer
from .models import Order
from .models import Products

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)
