from django.db import models


class Project(models.Model):
    """Model definition for Project."""

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)

    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="projects")

    client = models.CharField(max_length=50)
    website = models.CharField(max_length=250, blank=True, null=True)
    banner = models.ImageField(upload_to="portfolio/banners")
    cover = models.ImageField(upload_to="portfolio/covers")

    description = models.TextField()

    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Project."""

        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        """Unicode representation of Project."""
        return f"{self.name}"

    def image(self):
        return self.images.first().image

    def previous(self):
        if self.pk == Project.objects.first().pk:
            return None

        return Project.objects.filter(pk__lt=self.pk).last()

    def next(self):
        if self.pk == Project.objects.last().pk:
            return None

        return Project.objects.filter(pk__gt=self.pk).first()


class ProjectPoint(models.Model):
    """Model definition for ProjectPoint."""

    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="points")
    point = models.CharField(max_length=250)

    class Meta:
        """Meta definition for ProjectPoint."""

        verbose_name = "ProjectPoint"
        verbose_name_plural = "ProjectPoints"

    def __str__(self):
        """Unicode representation of ProjectPoint."""
        return f"{self.point}"


class ProjectImage(models.Model):
    """Model definition for ProjectImage."""

    image = models.ImageField(upload_to="portfolio/images")
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="images")

    class Meta:
        """Meta definition for ProjectImage."""

        verbose_name = "ProjectImage"
        verbose_name_plural = "ProjectImages"

    def __str__(self):
        """Unicode representation of ProjectImage."""
        return f"{self.project.name}"


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return f"{self.name}"
