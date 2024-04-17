from modeltranslation.translator import register, TranslationOptions

from server.apps.portfolio.models import Category, Project, ProjectPoint


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("az", "en", "ru")


@register(ProjectPoint)
class ProjectPointTranslationOptions(TranslationOptions):
    fields = ("point",)
    required_languages = ("az", "en", "ru")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description", "client")
    required_languages = ("az", "en", "ru")
