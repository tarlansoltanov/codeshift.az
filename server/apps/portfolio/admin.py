from django.contrib import admin
from .models import Project, ProjectImage, Category, ProjectPoint


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


class ProjectPointInline(admin.StackedInline):
    model = ProjectPoint
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'category', 'client', 'website')
    inlines = [ProjectImageInline, ProjectPointInline]
