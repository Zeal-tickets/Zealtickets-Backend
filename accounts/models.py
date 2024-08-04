from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import re
from zealtickets import settings

def validate_date_of_birth(value):
    # Check if the date is in the future
    if value > timezone.now().date():
        raise ValidationError("Date of birth cannot be in the future.")
    
    # Check if the age is less than 9 years
    min_age = 9
    if timezone.now().date() - value < datetime.timedelta(days=min_age * 365):
        raise ValidationError(f"Age must be at least {min_age} years old.")  



def validate_phone_number(value):  
    pattern = r'^\+?\d{1,4}?[-.\s]?(\(?\d{1,3}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    
    if not re.match(pattern, value):
        raise ValidationError("Invalid phone number format.")

    

        

class CustomBaseUserManager(BaseUserManager):
     def _create_user(self, password, **extra_fields):

        user = self.model(
                          **extra_fields
                          )        
        user.set_password(password)
        user.save(using=self.db)
        return user
     
     def create_superuser(self,password, **extrafields):
         
        new_account = self._create_user(password, **extrafields)

        new_account.is_active = True
        new_account.is_superuser = True
        new_account.is_staff = True
        new_account.save()

        return new_account

class User (AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    username  = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField()   
    d_o_b = models.DateField(null=True, validators=[validate_date_of_birth])
    phone_number = models.CharField(max_length=16, validators=[validate_phone_number])
    role = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    otp = models.CharField(max_length=7, blank=True)
    otp_max_try =models.CharField(max_length=2, default=settings.DEFAULT_OTP_MAX_TRY)
    otp_out=models.DateTimeField(null=True)
    otp_expiry = models.DateTimeField(null=True)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateField(auto_now_add=True)

    REQUIRED_FIELDS = ['phone_number','password']
    USERNAME_FIELD = 'username'

    object = CustomBaseUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class SellerProfile(models.Model):
    name   = models.CharField(max_length=100, blank=False)
    ownership = models.CharField(max_length=50)

    # TODO: Add upload to logos
    logo = models.FileField()
    email = models.EmailField()
    address = models.TextField(max_length=400)
     
    phone_number = models.CharField(max_length=16, validators=[validate_phone_number])

    website_url = models.CharField(max_length=1000, blank=True)
    office = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

