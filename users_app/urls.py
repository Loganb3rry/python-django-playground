from django.urls import path
from users_app import views

# Template URL's
app_name = 'user_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login"),
]
