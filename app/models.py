from django.db import models

class Informations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)  # Changed to CharField for phone number
    text = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
