from django.db import models

class Informations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)  # Changed to CharField for phone number
    text = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    des  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Collages(models.Model):
    name = models.CharField(max_length=120)
    collage_no=models.IntegerField()
    city=models.CharField(max_length=120)
    iet_no=models.IntegerField()
    
     
    def __str__(self):
        return self.name
    
    
    
class Teacher(models.Model):
    name =models.CharField(max_length=50)
    subject = models.CharField(max_length=60)
    age =models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
    
class principal(models.Model):
    name=models.CharField(max_length=10)
    class_room = models.IntegerField()
    subject = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name