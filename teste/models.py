from django.db import models

# Create your models here.


class Fornecedores(models.Model):
    name = models.CharField('Fornecedor', max_length=200)

    def __str__(self):
        return self.name
