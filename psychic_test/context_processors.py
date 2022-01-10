from .models import PsychicNumbers, Physic
from .services import get_history_assumptions_for_psychic, \
    get_history_user_numbers, get_last_confidence_level


def statistics(request):
    statistics = {
        'history_assumptions': [],
        'user_numbers': [],
        'physics_confidence_level': []
    }
    psychics = Physic.objects.all()
    for psychic in psychics:
        history_assumptions = get_history_assumptions_for_psychic(
            request.session.session_key,
            psychic.pk
        )
        statistics['history_assumptions'].append(history_assumptions)

    statistics['user_numbers'] = get_history_user_numbers(
        request.session.session_key
    )

    for psychic in psychics:
        last_confidence_level = get_last_confidence_level(
            request.session.session_key,
            psychic.pk
        )
        statistics['physics_confidence_level'].append((
            psychic.name, last_confidence_level))
    return {
        'statistics': statistics
    }
