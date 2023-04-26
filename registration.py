from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(password)
            user.username = username
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
