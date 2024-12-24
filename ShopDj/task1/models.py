from django.db import models

# Create your models here.

# Создайте в приложении task1 следующие модели:
#
# 1.Buyer - модель представляющая покупателя.
# Обладает следующими полями:
# name - имя покупателя(username аккаунта)
# balance - баланс(DecimalField)
# age - возраст.
#
# 2.Game - модель представляющая игру.
# Обладает следующими полями:
# title - название игры
# cost - цена(DecimalField)
# size - размер файлов игры(DecimalField)
# description - описание(неограниченное кол-во текста)
# age_limited - ограничение возраста 18+ (BooleanField, по умолчанию False)
# buyer - покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра
#           и у каждой игры может быть несколько обладателей.
# DecimalField - поле для дробных чисел.
# BooleanField - поле для булевых значений.


class Buyer(models.Model):
    name = models.CharField(max_length = 15)
    balance = models.DecimalField(max_digits=6,decimal_places = 2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length = 15)
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    size = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

