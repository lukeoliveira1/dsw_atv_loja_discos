from django.db import models

# Create your models here.
class GenderChoices(models.TextChoices):
    ROCK = "Rock"
    POP = "Pop"
    MPB = "Mpb"
    SERTANEJO = "Sertanejo"

class PhonographicSeal(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Nome",
    )

    def __str__(self):
        return self.name

class Disk(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Nome"
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Descrição",
        blank=True,
        null=True
    )
    phonographic_seal = models.ForeignKey(
        PhonographicSeal,
        on_delete=models.CASCADE,
        verbose_name="Selo Fotográfico",
        blank=True,
        null=True
    )
    year = models.IntegerField(
        verbose_name="Ano"
    )
    country = models.CharField(
        max_length=30,
        verbose_name="País"
    )
    gender = models.CharField(
        max_length=30,
        choices=GenderChoices.choices,
        verbose_name="Gênero"
    )
    quantity = models.IntegerField(
        verbose_name="Quantidade"
    )

    def __str__(self):
        return self.name
    

class Artist(models.Model):
    
    name = models.CharField(
        max_length=50,
        verbose_name="Nome",
    )
    
    disk = models.ManyToManyField(
        Disk,
        verbose_name="Discos",
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
