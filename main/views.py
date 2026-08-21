from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConsultationForm, CallbackForm, ContactForm


def home(request):
    consult_form = ConsultationForm()
    callback_form = CallbackForm()
    consult_success = False
    callback_success = False

    if request.method == 'POST':
        if 'consultation_submit' in request.POST:
            consult_form = ConsultationForm(request.POST)
            if consult_form.is_valid():
                consult_form.save()
                consult_success = True
                consult_form = ConsultationForm()

        elif 'callback_submit' in request.POST:
            callback_form = CallbackForm(request.POST)
            if callback_form.is_valid():
                callback_form.save()
                callback_success = True
                callback_form = CallbackForm()

    context = {
        'consult_form': consult_form,
        'callback_form': callback_form,
        'consult_success': consult_success,
        'callback_success': callback_success,
        'page': 'home',
    }
    return render(request, 'main/home.html', context)


def about(request):
    context = {'page': 'about'}
    return render(request, 'main/about.html', context)


def services(request):
    context = {'page': 'services'}
    return render(request, 'main/services.html', context)


def contact(request):
    contact_form = ContactForm()
    contact_success = False

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_success = True
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        'contact_success': contact_success,
        'page': 'contact',
    }
    return render(request, 'main/contact.html', context)
