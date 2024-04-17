from server.apps.base.models import Contact


def contact_details(request):
    contacts = Contact.objects.first()

    return {
        "email": contacts.email if contacts else "",
        "phone": contacts.phone if contacts else "",
        "address": contacts.address if contacts else "",
        "instagram": contacts.instagram if contacts else "",
        "facebook": contacts.facebook if contacts else "",
    }
