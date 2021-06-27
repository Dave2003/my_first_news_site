from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.crete, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update')
]
