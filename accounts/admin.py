from django.contrib import admin
from .models import User, SellerProfile


# Register your models here.
admin.register(User)
admin.site.register(SellerProfile)