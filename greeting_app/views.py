from django.shortcuts import render
from greeting_app.models import Topic, WebPage, AccessRecord


def index(request):
    web_pages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_pages_list}
    return render(request, 'greeting_app/index.html', context=date_dict)
