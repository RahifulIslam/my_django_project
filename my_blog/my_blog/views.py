from django.http import HttpResponse


def Index(request):
    return HttpResponse("I am in homepage")