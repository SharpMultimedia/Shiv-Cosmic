from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    paid = models.BooleanField(default=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    instamojo_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.payment_id