from django.db import models

class Transaction(models.Model):
    fullnames = models.CharField(max_length=200)
    amount = models.IntegerField()
    datetime = models.DateTimeField()
    payment_method = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    confirmation_code = models.CharField(max_length=60)