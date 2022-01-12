import json
import random

CONFIDENCE_DELTA = 10


def start_app_session(request) -> None:
    """Установит новую сессию на 4 часа и запишет в нее заготовку структуры
    данных"""
    # Сессия на 4 часа
    request.session.set_expiry(14400)
    # Заготовка структуры данных
    app_data = {
        'psychics': [
            {
                'name': 'Ванга',
                'assumptions': [],
                'confidence_level': 0
            },
            {
                'name': 'Распутин',
                'assumptions': [],
                'confidence_level': 0
            }
        ],
        'user': []
    }
    # Отправим данные в сессию
    request.session['app_data'] = json.dumps(app_data)
    print(request.session['app_data'])
    return None


def get_psychic_assumptions(request) -> list:
    """Получит предположения экстрасенсов и сохранит их в сессию.
    Также проверит, выдвигали ли предположения экстрасенсы на данном этапе
    """
    assumptions = []
    app_data = get_app_data_from_session(request)
    count_psychic_assumptions = len(app_data['psychics'][0]['assumptions'])
    count_user_answers = len(app_data['user'])

    # Если экстрасенсы уже предположили, а пользователь не написал свое,
    # то вернуться актуальные предположения
    if count_psychic_assumptions > count_user_answers:
        for key, psychic in enumerate(app_data['psychics']):
            assumptions.append((psychic['name'], psychic['assumptions'][-1],
                                key))
    else:
        for key, psychic in enumerate(app_data['psychics']):
            this_number = random.randint(10, 99)
            assumptions.append((psychic['name'], this_number, key))
        store_assumptions_to_session(request, assumptions)

    return assumptions


def get_app_data_from_session(request):
    """Получит данные из сессии"""
    return json.loads(request.session['app_data'])


def store_assumptions_to_session(request, psychics: list):
    """Сохранит предположения экстрасенсов в структуру сессии"""
    try:
        app_data = get_app_data_from_session(request)
        for psychic in psychics:
            assumption = psychic[1]
            key_in_app_data = psychic[2]
            app_data['psychics'][key_in_app_data]['assumptions'].append(
                assumption)
        request.session['app_data'] = json.dumps(app_data)
    except:
        raise ValueError("Не могу сохранить предположения в сессию")


def store_user_answer(request, number: int):
    """Сохранит ответ пользователя в структуру данных в сессии"""
    try:
        app_data = get_app_data_from_session(request)
        app_data['user'].append(number)
        request.session['app_data'] = json.dumps(app_data)
    except:
        raise ValueError("Не могу сохранить ответ пользователя в сессию")


def check_psychics(request, user_number: int):
    """Проверит экстрасенсов и внесет необходимые данные в сессию"""
    app_data = get_app_data_from_session(request)
    for key, psychic in enumerate(app_data['psychics']):
        confidence_level = psychic['confidence_level']
        if user_number == psychic['assumptions'][-1]:
            app_data['psychics'][key][
                'confidence_level'] = confidence_level + CONFIDENCE_DELTA
        else:
            app_data['psychics'][key][
                'confidence_level'] = confidence_level - CONFIDENCE_DELTA
    request.session['app_data'] = json.dumps(app_data)


def get_work_statistics(request):
    """Получит статистику и преобразует ее в нужную структуру для показа"""
    work_statistics = {
        'physics_confidence_level': [],
        'history_assumptions': [],
        'user_numbers': [],
    }
    app_data = get_app_data_from_session(request)
    for psychic in app_data['psychics']:
        work_statistics['physics_confidence_level'].append(
            (
                psychic['name'],
                psychic['confidence_level']
            )
        )
        work_statistics['history_assumptions'].append(
            (
                psychic['name'],
                psychic['assumptions']
            )
        )
    work_statistics['user_numbers'].append(
        app_data['user']
    )
    return work_statistics
