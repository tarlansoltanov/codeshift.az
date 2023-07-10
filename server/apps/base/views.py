from django.shortcuts import render, HttpResponse, redirect
from django.utils import translation

from .models import Message
from .forms import MessageForm

from ..portfolio.models import Project


def index(request):
    translation.activate('az')
    return redirect('base:home')

def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'

    context['projects'] = Project.objects.all().order_by('-modified_at')[:3]

    return render(request, template_name, context)


def about(request, template_name='base/about.html', context={}):
    context['title'] = 'About'
    return render(request, template_name, context)


def contact(request, template_name='base/contact.html', context={}):
    context['title'] = 'Contact'

    form = MessageForm(request.POST or None)

    if request.method == 'POST' and request.accepts("application/json"):
        if form.is_valid():
            form.save()

            return HttpResponse('Message sent successfully')

        return HttpResponse('Please fill all the fields correctly!', status=400)

    return render(request, template_name, context)