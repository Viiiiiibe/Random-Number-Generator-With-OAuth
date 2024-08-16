from django.shortcuts import render


def index(request):
    return render(request, 'random_number_generator/index.html')
