from django.db import models

# Create your models here.
class mycontact(models.Model):
    fname = models.CharField(max_length=50,default="")
    email = models.EmailField(default="")
    msg = models.TextField(max_length=300,default="")
    
    def __str__(self):
        return self.email