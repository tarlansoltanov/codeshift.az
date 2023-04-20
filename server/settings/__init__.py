from split_settings.tools import include, optional
from .components import config

ENV = config('DJANGO_ENV', default='local')

base_settings = (
    'components/common.py',         # Common settings
    'components/database.py',       # Database settings

    # Select the right env if it exists:
    f'environments/{ENV}.py',
)

# Include settings:
include(*base_settings)