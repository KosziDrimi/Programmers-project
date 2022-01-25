from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Programmer
from .forms import ProgrammerForm, LanguageForm


def index(request):
    return render(request, 'languages/index.html')


def add(request):
    if request.method == 'POST':
        form = ProgrammerForm(request.POST)
    
        if form.is_valid():
            try:
                Programmer.objects.filter(email=form.cleaned_data['email']).get()
                messages.warning(request, 'Programmer with this e-mail address has already been added.')
            except ObjectDoesNotExist:
                form.save()
                messages.success(request, 'New programmer added successfully!')
    
            return redirect('index')

    else:
        form = ProgrammerForm()

    context = {'form': form}
    return render(request, 'languages/add_form.html', context)


def show(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            languages = Programmer.objects.filter(c_plus_plus_level__gte=data['c_plus_plus_level'],
                                                  java_level__gte=data['java_level'], rust_level__gte=data['rust_level'],
                                                  python_level__gte=data['python_level'], c_level__gte=data['c_level'])

            context = {'languages': languages}
            return render(request, 'languages/result.html', context)

    else:
        form = LanguageForm()

    context = {'form': form}
    return render(request, 'languages/show_form.html', context)


def update(request, pk):
    programmer = Programmer.objects.get(id=pk)
    form = ProgrammerForm(instance=programmer)

    if request.method == 'POST':
        form = ProgrammerForm(request.POST, instance=programmer)

        if form.is_valid():
            form.save()
            messages.warning(request, 'The entry has been updated.')
            context = {'languages': [programmer]}
            return render(request, 'languages/result.html', context)

    context = {'form': form}
    return render(request, 'languages/update_form.html', context)
