import random

from .models import Physic, PsychicNumbers


def get_psychic_assumptions(session_key: str):
    """Получит предположения экстрасенсов"""
    assumptions = []
    physics = Physic.objects.all()
    for physic in physics:
        this_number = random.randint(0, 99)
        PsychicNumbers.objects.create(
            psychic=Physic(pk=physic.pk),
            user_session=session_key,
            number=this_number,
            confidence_level=0
        )
        assumptions.append((physic.name, this_number))
    # print(physics)
    return assumptions
