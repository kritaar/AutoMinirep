# config/settings.py
from pathlib import Path
import os

# =========================
# Rutas base
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Seguridad / Debug
# =========================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-no-uses-esto-en-produccion")
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "72.60.56.56",
]

# Si accedes por IP/puerto, declara los orígenes CSRF con esquema
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://72.60.56.56",
    "http://72.60.56.56:8000",
    "http://72.60.56.56:8001",
]

# =========================
# Apps
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "widget_tweaks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# =========================
# Templates
# =========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # /templates del proyecto
        "APP_DIRS": True,                  # /templates dentro de cada app
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# =========================
# Base de datos (Postgres por defecto)
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PGDATABASE", "tenant_autominirep"),
        "USER": os.getenv("PGUSER", "admin"),
        "PASSWORD": os.getenv("PGPASSWORD", "1234"),
        "HOST": os.getenv("PGHOST", "72.60.56.56"),
        "PORT": os.getenv("PGPORT", "55432"),
        "CONN_MAX_AGE": 60,  # keep-alive simple
    }
}
# Para usar SQLite local, comenta lo de arriba y descomenta:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# =========================
# Passwords
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# I18N / TZ
# =========================
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Lima"
USE_I18N = True
USE_TZ = True

# =========================
# Archivos estáticos
# =========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]   # aquí vive Tailwind: static/css/app.css
STATIC_ROOT = BASE_DIR / "staticfiles"     # para collectstatic en producción

# =========================
# Login / Logout
# =========================
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"

# =========================
# Otros
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Detrás de proxy/https (cuando uses Nginx/Proxy Manager):
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SESSION_COOKIE_SECURE = not DEBUG
# CSRF_COOKIE_SECURE = not DEBUG
