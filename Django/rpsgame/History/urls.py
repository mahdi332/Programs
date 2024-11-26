from django.urls import path
from . import views
app_name="History"
urlpatterns=[
    path("",views.history,name="history")
]