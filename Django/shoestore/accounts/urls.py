from django.urls import path
from . import views
app_name='accounts'
urlpatterns=[
    path('signin_section/',views.signin_section,name='signin_section'),
    path('signin_view/',views.signin_view, name='signin_view'),
    path('login_section/',views.login_section, name='login_section'),
    path('login_view/', views.login_view , name='login_view'),
    path('logout/',views.logout_view , name='logout_view')
]