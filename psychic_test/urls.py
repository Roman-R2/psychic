from django.urls import path

from .views import index, psychic_assumption, user_answer

app_name = 'psychic_test'

urlpatterns = [
    path('', index, name='index'),
    path(
        'psychic_assumption/',
        psychic_assumption,
        name='psychic_assumption'
    ),
    path('user_answer/', user_answer, name='user_answer')
]
