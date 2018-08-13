import os

from django.conf import settings


ENGINES = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}

def config():
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')

    if service_name:
        engine = ENGINES.get(os.getenv('DATABASE_ENGINE'), ENGINES['sqlite'])
    else:
        engine = ENGINES['sqlite']

    name = os.getenv('DATABASE_NAME')
    if not name and engine == ENGINES['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
    }
