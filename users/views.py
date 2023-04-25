from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View

from .forms import RegistrationForm


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html', {})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('starting-page')
        else:
            messages.success(request, ('There was an error logging in!'))
            return redirect('login-page')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ('You have been logged out'))
        return redirect('starting-page')
    
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()

        context = {
            'form': form,
        }

        return render(request, 'users/register.html', context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('starting-page')

        else:
            return render(request, 'users/register.html', {
                'form': form,
            })