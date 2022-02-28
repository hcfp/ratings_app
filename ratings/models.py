from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Module(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

class ModuleInstance(models.Model):
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    year = models.CharField(max_length=2)
    semester = models.CharField(max_length=2)

class ModuleLeaders(models.Model):
    module = models.ForeignKey("ModuleInstance", on_delete=models.CASCADE)
    professor = models.ForeignKey("Professors", on_delete=models.CASCADE)

class Professors(models.Model):
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

class Ratings(models.Model):
    professor = models.ForeignKey("Professors", on_delete=models.CASCADE)
    module_instance = models.ForeignKey("ModuleInstance", on_delete=models.CASCADE)
    score = models.IntegerField()