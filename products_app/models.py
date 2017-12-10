from django.db import models
from store_app.models import Storage
from documents_app.models import Document


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product (models.Model):
    code = models.IntegerField(unique=True,null=True, blank=True, default=None,verbose_name='Код товара')
    name = models.CharField(max_length=256, blank=False, verbose_name='Наименование товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    units = models.CharField(max_length=16, blank=True, null=True, verbose_name='Единицы измерения')
    provider_price = models.DecimalField(max_digits=20, decimal_places=2, default=0,verbose_name='Цена поставщика')
    vat = models.DecimalField(max_digits=6, decimal_places=2,default=20, verbose_name='НДС%')
    margin_percentage = models.DecimalField(max_digits=6, decimal_places=2,default=0, verbose_name='Торговая надбавка')
    product_price = models.DecimalField(max_digits=20, decimal_places=2,default=0, verbose_name='Розничная цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def __str__(self):
        return str(self.name)+'. Розничная цена: '+ str(self.product_price)


class Products(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товары в документах'
        verbose_name_plural = 'Товары в документах'

    def __str__(self):
        return str(self.product)+' '+ str(self.count)+' '+str(self.document)


class ProductMovement(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, verbose_name='Склад')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Количество')
    date = models.DateField(verbose_name='Дата операции')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ')
    operation_type = models.CharField(max_length=16)
    operation_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Движение товаров'
        verbose_name_plural = 'Движение товаров'

    def __str__(self):
        return str(self.date)+' '+ str(self.product)+' '+ str(self.count)+' '+str(self.storage)

