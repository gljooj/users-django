from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name="user_list"),
    path('<str:id>/', views.user_edit, name="user_edit"),
    path('new', views.user_new, name="user_new"),
    path('delete/<str:id>/', views.user_delete, name="user_delete"),
]
