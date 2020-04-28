from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Greetings from the Universe!")
    my_dict = {'insert_me': 'Hello, I am from views.py'}
    return render(request, 'greeting_app/index.html', context=my_dict)
