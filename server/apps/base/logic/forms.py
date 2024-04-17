from django import forms

from server.apps.base.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            "name",
            "email",
            "phone",
            "subject",
            "message",
        )
