from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def started_func(request):
    text_1 = 'Главная страница'
    context = {'text_1': text_1, }
    return render(request, 'temple_start.html', context)


def store_func(request):
    head_list = 'Список доступных товаров:'
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {'head_list': head_list,
               'games': games, }
    return render(request, 'temple_store.html', context)


def buy_func(request):
    text_head = 'Денег нет, но вы держитесь'
    context = {'text_head': text_head, }
    return render(request, 'temple_buy.html', context)


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']
            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'registration_page_django.html', {'form': form})
