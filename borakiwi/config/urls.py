from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("game/", views.gameing),
    path("main/", admin.main),
    path("over_win/", admin.over_win),
    path("over_lose/", admin.over_lose),
]
