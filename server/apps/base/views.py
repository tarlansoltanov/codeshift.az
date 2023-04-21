from django.shortcuts import render


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'
    return render(request, template_name, context)


def about(request, template_name='base/about.html', context={}):
    context['title'] = 'About'
    return render(request, template_name, context)