from django.db import models

# Create your models here.


# Create your models here.

class userinput(models.Model):
    EmpName = models.CharField(max_length=50)
    EmpID  =models.CharField(max_length=50)
    DOJ = models.DateField()
    TrainingDuration = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.EmpName    