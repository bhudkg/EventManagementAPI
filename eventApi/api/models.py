from django.db import models

# Create your models here.
class Event(models.Model):
    TYPE = [
        ("s", "Shadi"),
        ("b", "Birthday"),
        ("a", "Aniversery"),
        ("f", "family_gathering"),
    ]
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=TYPE)
    date = models.DateField()
    venue = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
