from django.urls import path
from .views import create, homepage, get_url

urlpatterns = [
    path('create', create),
    path('', homepage),
    path('get-url', get_url)
]