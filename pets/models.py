from django.db import models
from datetime import datetime

class Pets(models.Model):
    #django orm and migrations takes care of the database side of things
    
    petname=models.CharField(max_length=20)
    posted_by=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=12)
    description=models.TextField()
    posted_at=models.DateTimeField(default=datetime.now(),blank=False)

    def __str__(self):
        return self.petname

    class Meta:
        verbose_name_plural="Pets"
        
        

