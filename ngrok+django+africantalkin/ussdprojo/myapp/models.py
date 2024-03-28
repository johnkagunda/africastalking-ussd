# In myapp/models.py
import uuid
from django.db import models

class BusinessIdea(models.Model):
    category = models.CharField(max_length=100)
    idea = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.idea

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    session_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=10, unique=False)

    @classmethod
    def generate_uid(cls):
        return uuid.uuid4()

from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000)  # Default balance is 1000
    loan_limit = models.DecimalField(max_digits=10, decimal_places=2, default=1000)  # Default loan limit is 1000

    def __str__(self):
        return f"Account for {self.user.name}"

