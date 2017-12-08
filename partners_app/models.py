from django.db import models

class Partner(models.Model):
    full_name = models.CharField(max_length=512, blank=False, verbose_name='Полное наименование')
    short_name = models.CharField(max_length=128, verbose_name='Сокращенное наименование')
    address = models.CharField(max_length=128, verbose_name='Адрес')
    taxpayer_number = models.IntegerField(verbose_name='УНП')
    bank_requisites = models.CharField(max_length=64, verbose_name='Банковские реквизиты')

    class Meta:
        verbose_name = 'Конрагент'
        verbose_name_plural = "Контрагенты"

    def __str__(self):
        return self.short_name