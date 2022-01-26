from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMV',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')
