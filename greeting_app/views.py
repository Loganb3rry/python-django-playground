from django.shortcuts import render
from greeting_app.models import Topic, WebPage, AccessRecord
from greeting_app import forms


def index(request):
    web_pages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_pages_list}
    return render(request, 'greeting_app/index.html', context=date_dict)


def form(request):
    return render(request, 'greeting_app/form.html')


def form_name_view(request):

    form_name = forms.FormName()

    if request.method == 'POST':
        form_name = forms.FormName(request.POST)

        if form_name.is_valid():
            print("Validation Success")
            print("Name:" + form_name.cleaned_data['name'])
            print("Email:" + form_name.cleaned_data['email'])
            print("Text:" + form_name.cleaned_data['text'])

    return render(request, 'greeting_app/form.html', {'form': form_name})
