from .models import Contact


def contact_details(request):
    if not Contact.objects.exists():
        return {
            "email": "",
            "phone": "",
            "address": "",
            "instagram": "",
            "facebook": ""
        }
        
    contacts = Contact.objects.first()

    return {
        "email": contacts.email,
        "phone": contacts.phone,
        "address": contacts.address,
        "instagram": contacts.instagram,
        "facebook": contacts.facebook
    }