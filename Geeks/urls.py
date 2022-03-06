from django.urls import path
from . import views


urlpatterns = [
    path('', views.formoo, name = 'register'),
    path('individual/', views.formoo1, name = 'registerindividual'),
    path('thankYou/', views.formoo, name = 'thankYou'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/',views.logoutUser, name='logout'),
    path('database/',views.database, name ='database')
]