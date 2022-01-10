from django.urls import path

from .views import index, psychic_assumption

app_name = 'psychic_test'

urlpatterns = [
    path('', index, name='index'),
    path(
        'psychic_assumption/',
        psychic_assumption,
        name='psychic_assumption'
    ),
]
