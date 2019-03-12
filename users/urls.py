from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import BlogersView, SubscribeView

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blogers/', BlogersView.as_view(), name='blogers'),
    path('subscribe/<int:pk>/', SubscribeView.as_view(), name='subscribe'),
]
