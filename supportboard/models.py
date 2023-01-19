from django.db import models
from django.contrib.auth.models import User


class SupportRequest(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Waiting', 'Waiting'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=254)
    description = models.TextField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_trainer', null=True)
    status = models.CharField(max_length=254, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return self.title
