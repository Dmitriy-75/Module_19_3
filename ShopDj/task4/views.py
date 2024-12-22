from django.shortcuts import render
from task1.models import Game

# Create your views here.

# Представление списка товаров:
# Вместо списка с названиями игр используйте коллекцию всех записей Game.
# Передавайте эту коллекцию также в context функции render.
# Шаблон измените так, чтобы выводилось "<название игры> | <описание игры>. Стоимость: <стоимость игры>" + кнопка.


def menu(request):
    title="Игровая платформа"
    text="Главная страница"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'fourth_task/main_page.html', context)


def basket(request):

    text1 = "Корзина"
    text2 = "Извините, Ваша корзина пуста"

    context = {
        "text1": text1,
        "text2": text2
    }
    return render(request, 'fourth_task/basket.html', context)


def shop(request):
    games = Game.objects.all()

    context = {
        # "games": ['Шахматы', 'Шашки', 'Шиша-беша'],
        "games": games,
    }
    return render(request, 'fourth_task/shop.html', context)




