from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from task1.models import Buyer, Game



# Create your views here.

# Представление регистрации:
# Вместо списка псевдо-пользователей получайте записи из таблицы Buyer.
# Измените условие регистрации так, чтобы пользователь добавлялся только в том случае, если его нет в коллекции Buyer.
# Здесь можно использовать цикл for для получения имён каждого пользователя.
# Добавление пользователя осуществите через метод create, передав в него необходимые данные из POST запроса.
# В итоге, при нажатии на кнопку записи с введёнными данными должны появляться в БД в зависимости от условий.
# Используйте DB Browser для проверки:
#     -Добавления записей в таблицу.
#     -Недобавления записи, если покупатель с таким именем (username - name) уже существует.


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        for i in users:
            if i.name == username:
                info['error'] = 'Пользователь уже  существует'

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        if not info:
            info['hello'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name=username, balance=balance, age=age)

        print(f'username={username}')
        print(f'password={password}')
        print(f'{balance}')
        print(f'age={age}')

        return render(request, "fifth_task/registration_page.html", info)

    return render(request, "fifth_task/registration_page.html", info)







# Регистрация пользователя через формы Django в данной задаче не задействована

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            for i in users:
                if i == username:
                    info['error'] = 'Пользователь уже  существует'

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            if not info:
                info['hello'] = f'Приветствуем, {username}!'

            print(f'username={username}')
            print(f'password={password}')
            print(f'age={age}')

            return render(request, "fifth_task/registration_page.html", info)

    return render(request, "fifth_task/registration_page.html", info)














