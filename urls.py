# chatbot/urls.py
from django.urls import path
from . import views

app_name = "chatbot"

urlpatterns = [
    path("", views.get_data, name="get_data"),
    path("submit",views.save_data,name="save_data")
]
