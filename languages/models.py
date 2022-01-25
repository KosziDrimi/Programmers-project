from django.db import models


level_choices = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    c_plus_plus_level = models.IntegerField(default=0, choices=level_choices)
    c_level = models.IntegerField(default=0, choices=level_choices)
    rust_level = models.IntegerField(default=0, choices=level_choices)
    python_level = models.IntegerField(default=0, choices=level_choices)
    java_level = models.IntegerField(default=0, choices=level_choices)

    def __str__(self):
        return f'<{self.name} {self.surname} - {self.position}>'
