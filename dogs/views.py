from django.shortcuts import render

from dogs.models import Dog


def index(requests):
    dog_list = Dog.objects.all()
    context = {
        'object_list': dog_list,
        'title': 'Главная'
    }
    return render(requests, 'dogs/index.html', context)


def contact(requests):
    context = {
        'title': 'Контакты'
    }
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('message')
        print(f'{name} ({email}):{message}')
    return render(requests, 'dogs/contacts.html', context)