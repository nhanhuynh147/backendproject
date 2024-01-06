from django.db import models

# Create your models here.
    
class Voltage(models.Model):
    name = models.CharField(max_length= 100)
    Value_AN = models.FloatField (default=0)
    Value_BN = models.FloatField (default=0)
    Value_CN = models.FloatField (default=0)
    Value_AB = models.FloatField (default=0)
    Value_BC = models.FloatField (default=0)
    Value_CA = models.FloatField (default=0)
    
class Current(models.Model):
    name = models.CharField(max_length=100)
    Value_AN = models.FloatField (default=0)
    Value_BN = models.FloatField (default=0)
    Value_CN = models.FloatField (default=0)
    Value_AB = models.FloatField (default=0)
    Value_BC = models.FloatField (default=0)
    Value_CA = models.FloatField (default=0)

class Power(models.Model):
    name = models.CharField(max_length=100)
    Value = models.FloatField(default=0)  
    
class test(models.Model):
    Value = models.CharField(max_length=100)
       
    