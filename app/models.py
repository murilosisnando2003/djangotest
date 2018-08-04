from django.db import models

# Create your models here.


class Fornecedores(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField(blank=True, default="")

    def __str__(self):
        return self.name
