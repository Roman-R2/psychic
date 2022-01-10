from django.shortcuts import render, redirect

from .forms import QuestionForm
from .services import get_psychic_assumptions, save_user_answer, check_psychics


def index(request):
    # Сессия на 4 часа
    if 'anonymous_user' not in request.session:
        request.session.set_expiry(14400)
        request.session['anonymous_user'] = True

    # print(request.session.session_key)

    if request.method == 'POST':
        return redirect("psychic_test:psychic_assumption")

    return render(request, 'psychic_test/index.html')


def psychic_assumption(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            save_user_answer(
                request.session.session_key,
                request.POST.get('number')
            )
            check_psychics(request.session.session_key)
            return redirect("psychic_test:index")
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'psychic_assumption': get_psychic_assumptions(
            request.session.session_key,
        )
    }
    return render(
        request,
        'psychic_test/psychic_assumption.html',
        context=context
    )


def user_answer(request):
    return None
