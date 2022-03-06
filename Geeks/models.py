import email
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Details(models.Model):
    nameleader=models.CharField(max_length=200)
    name1=models.CharField(max_length=200)
    name2=models.CharField(max_length=200)
    name3=models.CharField(max_length=200)
    name4=models.CharField(max_length=200, blank =True,null=True)
    name5=models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True)
    contact=models.CharField(max_length=10)
    rollno = models.IntegerField(max_length=6)
    rollno1 = models.IntegerField(max_length=6)
    rollno2 = models.IntegerField(max_length=6)
    rollno3 = models.IntegerField(max_length=6)
    rollno4 = models.IntegerField(max_length=6,blank= True,null=True)
    rollno5 = models.IntegerField(max_length=6,blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,max_length=150)
    gitLinkedinLink=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nameleader} ({self.email})'

    class Meta:
        verbose_name = 'Team Registration'

class IndividualForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contact=models.CharField(max_length=10)
    rollno = models.IntegerField(max_length=6)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,max_length=150)
    gitLinkedinLink=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Individual Registration'
    
