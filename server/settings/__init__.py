from split_settings.tools import include

from server.settings.components import config

ENV = config("DJANGO_ENV", default="local")

base_settings = (
    "components/common.py",  # Common settings
    "components/database.py",  # Database settings
    "components/internationalization.py",  # Internationalization settings
    # Select the right env if it exists:
    f"environments/{ENV}.py",
)

# Include settings:
include(*base_settings)
