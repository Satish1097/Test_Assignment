from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.IntegerField()

    def __str__(self):
        return self.name
        
choice=[
    ("PENDING","Pending"),
    ("DONE","Done")
]
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    taskdetail=models.CharField(max_length=1000)
    tasktype = models.CharField(max_length=9,choices=choice,default="Pending")
    def __str__(self):
        return self.taskdetail
