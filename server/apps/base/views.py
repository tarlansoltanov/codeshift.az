from django.shortcuts import render


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'
    return render(request, template_name, context)