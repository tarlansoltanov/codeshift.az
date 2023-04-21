from django.db import models


class Contact(models.Model):
    """Model definition for Contact."""

    email = models.EmailField("Email", max_length=254)
    phone = models.CharField("Phone", max_length=50)
    address = models.CharField("Address", max_length=50)
    instagram = models.URLField("Instagram URL", max_length=200)
    facebook = models.URLField("Facebook URL", max_length=200)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact Details'
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        """Unicode representation of Contact."""
        return f"Contact Details"
