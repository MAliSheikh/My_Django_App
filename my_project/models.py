from django.db import models

# Create your models here.

class contactinfo(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField()
    des=models.TextField()
    # def  __str__(self):
    #     return self.name,self.email,self.des