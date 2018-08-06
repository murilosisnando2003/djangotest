from django.db import models

# Create your models here.


class Fornecedores(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField(blank=True, default="")
    telefone = models.CharField(max_length=20, blank=True, default=1)
    STATUS_CHOICES = (
        ('1', 'Ativo'),
        ('2', 'Desativado'),
    )  
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    contato = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name
