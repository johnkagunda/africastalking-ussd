from django.db import models

class BusinessIdea(models.Model):
    category = models.CharField(max_length=50)
    average_capital = models.DecimalField(max_digits=10, decimal_places=2)
    idea = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.idea
