from django.db import models

# Create your models here.

class Cliente(models.Model):
    BANCOS_CHOICES = [
        ('pan', 'PAN'),
        ('facta', 'Facta'),
        ('safra', 'Safra'),
    ]
    

    SERVICO_CHOICES = [
        ('inss', 'INSS'),
        ('fgts', 'FGTS'),
    ]
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    banco = models.CharField(max_length=10, choices=BANCOS_CHOICES)
    servico = models.CharField(max_length=10, choices= SERVICO_CHOICES)

    
    def __str__(self):
        return f"{self.nome} - {self.banco} - {self.servico}"