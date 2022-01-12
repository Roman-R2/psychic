from django.urls import path

from .views import GreetingView, AnswerView

app_name = 'psychic_test'

urlpatterns = [
    path('', GreetingView.as_view(), name='index'),
    path(
        'psychic_assumption/',
        AnswerView.as_view(),
        name='psychic_assumption'
    ),
]
