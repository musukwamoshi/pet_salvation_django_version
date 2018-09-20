from django.db import models
from datetime import datetime

class Pets(models.Model):
    #django orm and migrations takes care of the database side of things
    
    petname=models.CharField(max_length=20)
    poster=models.CharField(max_length=100)
    email=models.CharField(max_length=254)
    phone_number=models.CharField(max_length=12)
    area=models.CharField(max_length=30)
    town=models.CharField(max_length=30)
    province=models.CharField(max_length=30)
    description=models.TextField()
    filename=models.FileField(upload_to='media/')
    posted_at=models.DateTimeField(default=datetime.now(),blank=False)

    def __str__(self):
        return self.petname

    class Meta:
        verbose_name_plural="Pets"
        
        

