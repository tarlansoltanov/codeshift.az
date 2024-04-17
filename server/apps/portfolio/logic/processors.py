from server.apps.portfolio.models import Category


def categories(request):
    """Add categories to context."""
    categories = Category.objects.all()
    return {"categories": categories}
