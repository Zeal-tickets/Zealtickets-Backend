from django.db import models
from django.contrib.auth.models import  AbstractBaseUser

#  TODO: Do a user base manager.

class User (AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    username  = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField()

    # TODO: Validation one shoul not set a date more than the current date and also it should be not be the past 16 years
    d_o_b = models.DateField()

    # TODO:Come up with  validation formart of phone number using regex 7XXXXXXXX
    phone_number = models.CharField(max_length=16)
    role = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    otp = models.CharField(max_length=7, blank=True)
    otp_max_try =models.CharField(max_length=2)
    otp_out=models.DateTimeField()
    otp_expiry = models.DateTimeField()

    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()

    date_joined = models.DateField()

    REQUIRED_FIELDS = ['phone_number','password']
    USERNAME_FIELD = 'username'

class SellerProfile(models.Model):
    name   = models.CharField(max_length=100, blank=False)
    ownership = models.CharField(max_length=50)

    # TODO: Add uplod to logos
    logo = models.FileField()
    email = models.EmailField()
    address = models.TextField(max_length=400)
     

    # TODO:use the validation to be created
    phone_number = models.CharField(max_length=16)

    website_url = models.CharField(max_length=1000, blank=True)
    office = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

