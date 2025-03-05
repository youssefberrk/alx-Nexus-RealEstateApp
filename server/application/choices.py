from django.db import models


class ApplicationStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    DENIED = 'Denied', 'Denied'
    APPROVED = 'Approved', 'Approved'

class PaymentStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    PAID = 'Paid', 'Paid'
    PARTIALLY_PAID = 'PartiallyPaid', 'Partially Paid'
    OVERDUE = 'Overdue', 'Overdue'
