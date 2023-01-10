from django.db import models
from django.contrib.auth.models import User


class SupportRequest(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
