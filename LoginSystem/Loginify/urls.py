from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('get-all-users/', views.get_all_users, name='get_all_users'),
    path('get-user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('update-user/<str:email>/', views.update_user, name='update_user'),
    path('delete-user/<str:email>/', views.delete_user, name='delete_user'),
]
