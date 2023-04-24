from django.shortcuts import render, HttpResponse
from ..portfolio.models import Project
from .models import Message


def home(request, template_name='base/index.html', context={}):
    context['title'] = 'Home'

    context['projects'] = Project.objects.all()[:4]

    return render(request, template_name, context)


def about(request, template_name='base/about.html', context={}):
    context['title'] = 'About'
    return render(request, template_name, context)


def contact(request, template_name='base/contact.html', context={}):
    context['title'] = 'Contact'

    if request.method == 'POST' and request.accepts("application/json"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and phone and subject and message:
            Message.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            return HttpResponse('Message sent successfully')

        return HttpResponse('Please fill all the fields', status=400)

    return render(request, template_name, context)