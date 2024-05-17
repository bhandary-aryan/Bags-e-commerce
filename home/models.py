from django.db import models

# makemigrations means create changes and store in a file
# migrate means apply all the changes made created by make migrations

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=10)
    feedback= models.TextField()
    date= models.DateField()
    
    
    # this function will show the contact with their name in admin section
    def __str__(self):
        return self.name