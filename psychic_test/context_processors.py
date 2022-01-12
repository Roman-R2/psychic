from .services import get_work_statistics


def statistics(request):
    work_statistics = get_work_statistics(request)

    return {
        'statistics': work_statistics
    }
