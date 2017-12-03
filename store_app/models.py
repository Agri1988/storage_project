from django.db import models

class Storage(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название склада')
    address = models.CharField(max_length=256, verbose_name='Адрес склада')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = "Склады"
    def __str__(self):
        return str(self.name)
