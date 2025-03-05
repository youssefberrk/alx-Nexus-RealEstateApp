from .choices import ApplicationStatus, PaymentStatus
from django.db import models
from django.contrib.auth import get_user_model
from property.models import Property

User = get_user_model()


class Lease(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Foreign keys
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leases')
    
    def __str__(self):
        return f"Lease for {self.property.name} - {self.tenant.name}"

class Application(models.Model):
    application_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=ApplicationStatus.choices)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    
    # Foreign keys
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='applications')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    lease = models.OneToOneField(Lease, on_delete=models.SET_NULL, null=True, blank=True, related_name='application')
    
    def __str__(self):
        return f"Application for {self.property.name} by {self.name}"

class Payment(models.Model):
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices)
    
    # Foreign key
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    
    def __str__(self):
        return f"Payment for {self.lease} - {self.amount_paid}/{self.amount_due}"

