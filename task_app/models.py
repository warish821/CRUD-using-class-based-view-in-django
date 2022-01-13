from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=50,null=True)
    user_name = models.OneToOneField(Users,on_delete=models.CASCADE,related_name='user_name')
    description = models.TextField()

    def __str__(self):
        return self.title


