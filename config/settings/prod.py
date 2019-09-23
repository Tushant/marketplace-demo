from .base import *  # noqa

env.read_env(str(BASE_DIR.path('.env.prod')))

DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = []

DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405
