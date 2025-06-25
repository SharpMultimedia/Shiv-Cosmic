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
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Rekhi_Form(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class AstroBooking(models.Model):  
    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=20)  
    email = models.EmailField()  
    paid = models.BooleanField(default=False)  

    def __str__(self):
        return self.name        
    
class Report(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    pdf_url = models.URLField()
    report_type = models.CharField(max_length=50)  # To distinguish between basic/pro/numerology/vastu
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s {self.report_type} Report"