from django.urls import path
from .views import *


urlpatterns = [

    path('main/', main, name='main'),
    path('welcome', registerPage, name='register'),
    path('login/', loginForm, name='login'),
    path('logout/', logOut, name='logout'),
    path('filterdata/', filterData, name='filterdata'),
    path('data/<str:pk>/', showData, name='data'),

]