from django.shortcuts import render
from ..portfolio.models import Project


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'

    context['projects'] = Project.objects.all()[:4]

    return render(request, template_name, context)


def about(request, template_name='base/about.html', context={}):
    context['title'] = 'About'
    return render(request, template_name, context)


def contact(request, template_name='base/contact.html', context={}):
    context['title'] = 'Contact'
    return render(request, template_name, context)