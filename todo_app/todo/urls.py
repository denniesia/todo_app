from django.urls import path
from .views import sign_up, home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='sign_up'),
]


