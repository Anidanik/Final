from django.db import models
from django.contrib.auth.models import User
from main.models import Games


class CollectionUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class GameInCollection(models.Model):
    collection= models.ForeignKey(CollectionUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Games,on_delete= models.CASCADE,related_name='games')

    def __str__(self):
        return f'{self.game}'

    class Meta:
        verbose_name = 'Игра в коллекции'
        verbose_name_plural = 'Игры в коллекции'