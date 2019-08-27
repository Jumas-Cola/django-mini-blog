from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^(?P<pk>\d+)/create$', views.CommentCreate.as_view(), name='comment_create'),
    url(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    url(r'^bloggers/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
]
