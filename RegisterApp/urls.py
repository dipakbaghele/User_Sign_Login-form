from django.urls import path,include
from .import views
from .views import signup, show_home_page

urlpatterns = [
    path('signup/',views.login_view,name='Signup'),
    path('success/',views.success,name='message'),
    path('login/',views.UserLogin,name='login'),
    #path('home/',views.HomePage,name='Home'),
    path('profile/',views.Profile,name='profile'),
    path('logout/', views.UserLogout, name='logout'),
    path('',signup),
    path('show/',views.show_home_page),
]
