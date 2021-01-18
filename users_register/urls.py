from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name="user_list"),
    path('user/<str:id>/', views.user_edit, name="user_edit"),
    path('user', views.user_new, name="user_new"),
    path('delete/<str:id>/', views.user_delete, name="user_delete"),
]
