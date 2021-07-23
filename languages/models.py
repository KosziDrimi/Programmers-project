from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=20) 
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    position = models.CharField(max_length=30)
    c_plus_plus_level = models.IntegerField(default=0)
    c_level = models.IntegerField(default=0)
    rust_level = models.IntegerField(default=0)
    python_level = models.IntegerField(default=0)
    java_level = models.IntegerField(default=0)

    def __str__(self):
        return f'<{self.name} {self.surname} - {self.position}>'

