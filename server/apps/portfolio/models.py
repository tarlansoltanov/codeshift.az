from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField("Name", max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.name}'
