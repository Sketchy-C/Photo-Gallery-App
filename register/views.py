from django.shortcuts import render, redirect
from .forms import registerForm


def register(response):
    if response.method == 'POST':
        form = registerForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = registerForm()
    return render(response,'register/register.html',{'form':form})