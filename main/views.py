from django.shortcuts import render



def index(request):
    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели - Home'

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст про магазин'

    }
    return render(request, 'main/about.html', context)
