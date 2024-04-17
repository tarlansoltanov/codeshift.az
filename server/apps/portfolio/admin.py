from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from server.apps.portfolio.models import Category, Project, ProjectImage, ProjectPoint


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name",)
    group_fieldsets = True


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


class ProjectPointInline(TranslationStackedInline):
    model = ProjectPoint
    extra = 1


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    inlines = [ProjectImageInline, ProjectPointInline]

    group_fieldsets = True

    list_display = (
        "name",
        "title",
        "category",
        "client",
        "website",
    )
