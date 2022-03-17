from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("install/", views.install, name="install"),
    path("documentation/<str:page_name>/", views.documentation, name="documentation"),
]