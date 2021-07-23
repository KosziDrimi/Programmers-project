from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Programmer
from .forms import ProgrammerForm, LanguageForm


def index(request):
    return render(request, 'languages/index.html')


def add(request):
    
    if request.method == 'POST':
        form = ProgrammerForm(request.POST)
    
        if form.is_valid():
            new = Programmer(name = form.cleaned_data['name'],
                    surname = form.cleaned_data['surname'],
                    email = form.cleaned_data['email'],
                    position = form.cleaned_data['position'],
                    c_plus_plus_level = form.cleaned_data['c_plus_plus_level'],
                    c_level = form.cleaned_data['c_level'],
                    rust_level = form.cleaned_data['rust_level'],
                    python_level = form.cleaned_data['python_level'],
                    java_level = form.cleaned_data['java_level'])
            new.save()
            messages.success(request, 'New programmer added successfully!')
    
            return redirect('index')

    else:
        form = ProgrammerForm()

    context = {'form' : form}
    return render(request, 'languages/add_form.html', context)


def show(request):

    if request.method == 'POST':
        form = LanguageForm(request.POST)

        if form.is_valid():

            c_plus_plus_level = form.cleaned_data['c_plus_plus_level']
            c_level = form.cleaned_data['c_level']
            rust_level = form.cleaned_data['rust_level']
            python_level = form.cleaned_data['python_level']
            java_level = form.cleaned_data['java_level']

            languages = Programmer.objects.filter(c_plus_plus_level__gte = c_plus_plus_level,
                        c_level__gte = c_level, rust_level__gte = rust_level,
                        python_level__gte = python_level, java_level__gte = java_level)

            context = {'languages' : languages}
            return render(request, 'languages/result.html', context)

    else:
        form = LanguageForm()

    context = {'form' : form}
    return render(request, 'languages/show_form.html', context)
