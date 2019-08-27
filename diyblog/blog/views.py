from django.shortcuts import render
from .models import Blog, Blogger, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_comments = Comment.objects.all().count()

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


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerDetailView(generic.DetailView):
    model = Blogger


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)
