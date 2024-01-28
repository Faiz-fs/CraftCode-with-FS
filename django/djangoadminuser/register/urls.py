from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index,name="index"),
    path('register',views.regist,name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('profile',views.profile,name='profile'),
    path('logout',LogoutView.as_view(next_page='index'),name='logout')

]