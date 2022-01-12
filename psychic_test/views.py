from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import QuestionForm
from .services import get_psychic_assumptions, save_user_answer, \
    check_psychics, start_session


class GreetingView(TemplateView):
    template_name = 'psychic_test/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.session.is_empty():
            start_session(request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return redirect("psychic_test:psychic_assumption")


# def index(request):
#     if request.session.is_empty():
#         start_session(request)
#
#     if request.method == 'POST':
#         return redirect("psychic_test:psychic_assumption")
#
#     return render(request, 'psychic_test/index.html')

# class AnswerView(View):
#     template_name = 'psychic_test/psychic_assumption.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.session.is_empty():
#             return redirect("psychic_test:index")
#         return super().dispatch(request, *args, **kwargs)


def psychic_assumption(request):
    if request.session.is_empty():
        return redirect("psychic_test:index")

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
