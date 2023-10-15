from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE, related_name='mileage')

    mileage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.car if self.car else self.moto} - {self.milaege}'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ('-year',)


