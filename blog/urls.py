from django.urls import path
from . import views
urlpatterns = [
    path('', views.blogView, name='blog'),
    path('<slug:slug>/', views.blogSingleView, name='blog_single'),
    path('comment', views.comments,  name='comment'),
    path('search', views.search,  name='search'),
    path('newsletter', views.NewsLetter, name='newsletter')
]