from django.urls import path

# import views from the current directory 'main'
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
]
