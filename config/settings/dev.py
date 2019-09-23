from .base import *  # noqa

env.read_env(str(BASE_DIR.path('.env.dev')))

DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar"]  # noqa F405

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

INSTALLED_APPS += ["django_extensions"]  # noqa F405

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
