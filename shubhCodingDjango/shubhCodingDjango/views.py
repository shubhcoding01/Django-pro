from django.http import HttpResponse

def home(response):
    return HttpResponse("Hello..!! This is Shubh Coding World Home Pages..")

def about(response):
    return HttpResponse("Hello buddy..!! This is Shubh Coding World About Pages..")

def contact(response):
    return HttpResponse("Hello bro..!! This is Shubh Coding World Contact Pages..")