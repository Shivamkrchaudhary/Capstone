from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name= "login_pag"),
    # path("dashboard/", views.login_page, name="Dashboard")
]