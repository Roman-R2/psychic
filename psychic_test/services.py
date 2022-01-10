import random

from django.db.models import F

from .models import Physic, PsychicNumbers, UserNumbers


def get_confidence_levels():
    """Получим уровни достоверности каждого экстрасенса"""
    pass


def get_history_user_numbers(session_key: str, ):
    """Получит историю чисел пользователя"""
    this_numbers = UserNumbers.objects.filter(
        user_session=session_key,
    )
    return this_numbers


def get_history_assumptions_for_psychic(session_key: str, psychic_pk: int):
    """Получит историю догадок для экстрасенсы по его pk"""
    this_psychic = PsychicNumbers.objects.filter(
        psychic=Physic(pk=psychic_pk),
        user_session=session_key,
    )
    return this_psychic


def get_last_confidence_level(session_key: str, psychic_pk: int):
    """Получит последний уровень достоверности экстрасенса для определенного
    пользователя"""
    this_psychic = PsychicNumbers.objects.filter(
        user_session=session_key,
        psychic=Physic.objects.get(pk=psychic_pk)).last()
    if this_psychic:
        return this_psychic.confidence_level
    return 0


def get_psychic_assumptions(session_key: str) -> list:
    """Получит предположения экстрасенсов"""
    assumptions = []
    physics = Physic.objects.all()
    for psychic in physics:
        this_number = random.randint(0, 99)
        PsychicNumbers.objects.create(
            psychic=Physic(pk=psychic.pk),
            user_session=session_key,
            number=this_number,
            confidence_level=get_last_confidence_level(session_key, psychic.pk)
        )
        assumptions.append((psychic.name, this_number))
    return assumptions


def save_user_answer(session_key: str, number: int):
    """Сохранит ответ пользователя в базу данных"""
    UserNumbers.objects.create(
        user_session=session_key,
        number=number
    )
    return 1


def check_psychics(session_key: str):
    """Проверит экстрасенсов и внесет необходимые данные в базу данных"""
    this_user = UserNumbers.objects.filter(
        user_session=session_key,
        is_checked=False
    ).last()
    physics = Physic.objects.all()
    for psychic in physics:
        this_psychic = PsychicNumbers.objects.filter(
            psychic=psychic,
            user_session=session_key,
            is_checked=False
        ).last()
        if this_user.number == this_psychic.number:
            this_psychic.confidence_level = F('confidence_level') + 10
        else:
            this_psychic.confidence_level = F('confidence_level') - 10
        this_psychic.save()
    return None
