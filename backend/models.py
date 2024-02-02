from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона')
    contract = models.CharField(max_length=14, verbose_name='№ договора', blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Apartment(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер квартиры')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Обьект')
    floor = models.PositiveIntegerField(verbose_name='Этаж')
    square = models.FloatField(validators=(MinValueValidator(0.0),), verbose_name='Площадь')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    STATUS_CHOICES = (
        ('Активна', 'Активна'),
        ('Бронь', 'Бронь'),
        ('Куплено', 'Куплено'),
        ('Рассрочка', 'Рассрочка'),
        ('Бартер', 'Бартер'),
    )
    status = models.CharField(max_length=20, default='Активна', choices=STATUS_CHOICES, verbose_name='Статус')
    price = models.PositiveIntegerField(verbose_name='Цена')
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Клиент')
    date_status = models.DateField(null=True, blank=True, verbose_name='Дата статуса')

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return str(self.number)


class Manager(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    amount = models.PositiveIntegerField(verbose_name='Количество сделок')

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return self.name
