from django.urls import path

from .views import index

app_name = 'psychic_test'

urlpatterns = [
    path('', index, name='index'),
]
