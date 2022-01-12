from django.urls import path

from .views import psychic_assumption, GreetingView

app_name = 'psychic_test'

urlpatterns = [
    path('', GreetingView.as_view(), name='index'),
    path(
        'psychic_assumption/',
        psychic_assumption,
        name='psychic_assumption'
    ),
]
