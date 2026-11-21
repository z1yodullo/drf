from django.db import models

class Teachers(models.Model):
    name=models.CharField(max_length=255)
    experience=models.IntegerField()

class Courses(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    teacher=models.ForeignKey(Teachers,on_delete=models.CASCADE)

class Students(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)

