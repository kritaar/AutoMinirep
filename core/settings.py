from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # agrega tu IP pública cuando despliegues
