from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField('Имя', max_length=20)
    balance = models.DecimalField('Баланс', max_digits=5, decimal_places=2)
    age = models.PositiveSmallIntegerField('Возраст', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Покупатели'
        verbose_name = 'покупателя'
        ordering = ['name']


class Game(models.Model):
    title = models.CharField('Наименование', max_length=100)
    cost = models.DecimalField('Стоимость', max_digits=5, decimal_places=2)
    size = models.DecimalField('Размер', max_digits=5, decimal_places=2)
    description = models.TextField('Описание', )
    age_limited = models.BooleanField('Возрастной ценз', default=True)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Игры'
        verbose_name = 'игру'
        ordering = ['size']


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Текст')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        ordering = ['-date']
