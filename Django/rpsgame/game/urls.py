from django.urls import path
from . import views
app_name='game'
urlpatterns=[
    path('menu/', views.menu , name='menu'),
    path('gamesec/',views.gameview , name='gameview'),
    path('results/', views.results , name='results'),
]
