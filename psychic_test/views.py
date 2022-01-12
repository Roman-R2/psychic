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


class AnswerView(TemplateView):
    template_name = 'psychic_test/psychic_assumption.html'
    form_class = QuestionForm

    def _add_context_and_render(self, request, form):
        context = {
            'form': form,
            'psychic_assumption': get_psychic_assumptions(
                request.session.session_key,
            )
        }
        return render(
            request,
            self.template_name,
            context=context
        )

    def dispatch(self, request, *args, **kwargs):
        if request.session.is_empty():
            return redirect("psychic_test:index")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            save_user_answer(
                request.session.session_key,
                request.POST.get('number')
            )
            check_psychics(request.session.session_key)
            return redirect("psychic_test:index")
        return self._add_context_and_render(request, form)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self._add_context_and_render(request, form)
