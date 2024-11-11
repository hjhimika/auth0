# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('login', views.user_login, name='login'),
#     path('signup', views.user_signup, name='signup'),
    
#     path('logout', views.user_logout, name='logout'),
#     path("callback", views.callback, name="callback")
    
# ]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]