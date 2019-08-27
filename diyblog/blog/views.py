from django.shortcuts import render
# from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_blogs = 0 # Blog.objects.all().count()
    num_bloggers = 0 # Blogger.objects.all().count()
    num_comments = 0 # Comment.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_blogs': num_blogs,
            'num_bloggers': num_bloggers,
            'num_comments': num_comments,
            'num_visits': num_visits,
        },
    )
