from django.db import models
from django.contrib.auth.models import User

# Create your models
class Expense(models.Model):
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField()
    category=models.CharField(max_length=50)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
  