from decouple import config

from .base import *

if config('DEBUG', default=False, cast=bool):
    from .dev import *
else:
    from .prod import *
    # Heroku: Update database configuration from $DATABASE_URL.
    import dj_database_url

    DATABASES['default'] = dj_database_url.config(conn_max_age=500, ssl_require=True)

    # DATABASES['default'] = db_from_env
