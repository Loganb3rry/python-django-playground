from django.shortcuts import render
from users_app.forms import NewUserForm


def help(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request, 'users_app/help.html', context=help_dict)


def index(request):
    return render(request, 'users_app/index.html')


def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {"users": user_list}
    # return render(request, 'users_app/users.html', context=user_dict)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form Invalid')

    return render(request, 'users_app/users.html', {'form': form})
