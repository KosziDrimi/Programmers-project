from django.db import models
from django.core.validators import MaxValueValidator


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    c_plus_plus_level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    c_level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    rust_level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    python_level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    java_level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])

    def __str__(self):
        return f'<{self.name} {self.surname} - {self.position}>'
