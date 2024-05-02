from django.db import models


class Games(models.Model):
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, verbose_name='Издатель')
    name = models.CharField(max_length=30, verbose_name='Название игры')
    number_of_players = models.IntegerField(default=4, verbose_name='Рекомендуемое число игроков')
    grade = models.FloatField(verbose_name='Оценка игры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    mechanics = models.ManyToManyField('mechanics', verbose_name='Основные механики')
    serial_number = models.OneToOneField('SerialNumber', on_delete=models.SET_NULL, null=True, verbose_name='Серийный номер')

    def __str__(self):
        return f'{self.publisher}-{self.name}-{self.grade}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created_at']


class Publisher(models.Model):
    publisher = models.CharField(max_length=30, verbose_name='Название издателя')
    count = models.IntegerField()

    def __str__(self):
        return f'{self.publisher}'

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class SerialNumber(models.Model):
    number = models.CharField(max_length=9, verbose_name='серийный номер')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Серийный номер'
        verbose_name_plural = 'Серийные номера'


class Mechanics(models.Model):
    mechanics = models.CharField(max_length=30, verbose_name='Механика')

    def __str__(self):
        return f'{self.mechanics}'

    class Meta:
        verbose_name = 'Механика'
        verbose_name_plural = 'Механики'


