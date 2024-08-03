from django.db import models
from accounts.models import SellerProfile

 # !FIXME: Needs to be imported in accounts
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Event(models.Model):
    max_attendees = models.IntegerField()
    venue = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    description = models.TextField(max_length=2000)

    # TODO: Add upload to /posters field
    poster = models.FileField()
    
   
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    sellerprofile = models.ForeignKey(SellerProfile, on_delete=models.SET_NULL , null=True)


