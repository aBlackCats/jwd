from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("/data_baru", views.create, name="create"),
    path("/edit_data/<int:id>", views.edit, name="edit"),
    path("/hapus_data/<int:id>", views.hapus, name="hapus"),
    path("logout/", views.logout_view, name="logout"),
]
