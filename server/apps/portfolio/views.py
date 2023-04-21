from django.shortcuts import render


def index(request, template_name='portfolio/index.html', context={}):
    context['title'] = "Portfolio"
    return render(request, template_name, context)