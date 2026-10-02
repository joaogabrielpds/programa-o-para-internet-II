from django.http import HttpResponse


def index(request):
    return HttpResponse("Seja bem-vindo ao meu primeiro projeto Django!")
