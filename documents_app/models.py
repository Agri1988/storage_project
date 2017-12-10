from django.db import models
from store_app.models import Storage
from partners_app.models import Partner

class Document(models.Model):
    document_type_choise = [('add','Приходный документ'), ('remove', 'Расходный документ'), ('move', 'Перемещение')]
    document_type = models.CharField(max_length=128, choices=document_type_choise ,verbose_name='Тип документа')
    name = models.CharField(max_length=64, verbose_name='Наименование')
    serial = models.CharField(max_length=64, verbose_name='Серия')
    number = models.CharField(max_length=64, verbose_name='Номер')
    date = models.DateField(verbose_name='Дата документа')
    provider = models.ForeignKey(Partner,default=1, verbose_name='Поставщик')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, default='1', verbose_name='Склад')
    to_storage = models.ForeignKey(Storage, related_name='destination_storage',default=None, blank=True, null=True,
                                   verbose_name="Склад перемещения")
    document_status_execute = models.BooleanField(default=False ,verbose_name='Документ проведен')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.serial + self.number