from django.urls import path

from . import views
urlpatterns = [
    path('', views.TodosList, name='index'),
    path('<int:pk>/', views.TodoDetail, name='detail'),
    path('create/',views.TodoCreate, name='create'),
    path('<int:pk>/delete', views.TodoDelete, name='delete'),
    path('<int:pk>/done', views.TodoDone, name='done'),
    path('<int:pk>/update', views.TodoUpdate, name='update'),
]
