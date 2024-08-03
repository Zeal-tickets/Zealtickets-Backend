from django.db import models
from events.models import Event
from payment.models import Transaction

class Ticket(models.Model):
    amount = models.IntegerField()
    ticket_type = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    number = models.IntegerField()
    event = models.ForeignKey(Event , on_delete=models.SET_NULL , null=True)


class Purchase(models.Model):
    datetime = models.DateTimeField()
    payment_method = models.CharField(max_length=1000)
    UUID = models.CharField(max_length=300)
    status = models.CharField(max_length=50)
    
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)

    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)