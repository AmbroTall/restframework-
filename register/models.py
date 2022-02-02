from django.db import models

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    current_place = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.id}'

