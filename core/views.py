from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest):
    return HttpResponse("¡Hola, Django!")
