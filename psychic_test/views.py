from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'psychic_test/index.html', context=context)
