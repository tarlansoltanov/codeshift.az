from django.db import models


class Project(models.Model):
    """Model definition for Project."""

    name = models.CharField("Name", max_length=50)
    title = models.CharField("Title", max_length=250)
    description = models.TextField("Description")
    client = models.CharField("Client", max_length=50)
    category = models.ForeignKey("Category", verbose_name="Category", on_delete=models.CASCADE, related_name="projects")
    website = models.CharField("Website", max_length=250)

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Unicode representation of Project."""
        return f'{self.name}'


class ProjectImage(models.Model):
    """Model definition for ProjectImage."""

    image = models.ImageField("Image", upload_to='portfolio/images')
    project = models.ForeignKey("Project", verbose_name="Project", on_delete=models.CASCADE, related_name="images")

    class Meta:
        """Meta definition for ProjectImage."""

        verbose_name = 'ProjectImage'
        verbose_name_plural = 'ProjectImages'

    def __str__(self):
        """Unicode representation of ProjectImage."""
        return f'{self.project.name}'


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