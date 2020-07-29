from django.db import models
'''
Two modeles are created. 
Employee
Positon 
'''
class Position(models.Model):
    title = models.CharField(max_length=50)

    # show the title in position when selection
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)  # Foreign key is position, when delete the positon, employee will also be deleted.
     
