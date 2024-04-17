from django.db import models


class Contact(models.Model):
    """Model definition for Contact."""

    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    instagram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = "Contact Details"
        verbose_name_plural = "Contact Details"

    def __str__(self):
        """Unicode representation of Contact."""
        return "Contact Details"


class Message(models.Model):
    """Model definition for Message."""

    name = models.CharField(max_length=50)

    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)

    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Message."""

        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        """Unicode representation of Message."""
        return self.name
