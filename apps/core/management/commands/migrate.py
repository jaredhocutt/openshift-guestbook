from django.conf import settings
from django.core.management.commands import migrate


class Command(migrate.Command):
    def handle(self, *args, **options):
        db_settings = settings.DATABASES[options['database']]

        if 'sqlite' not in db_settings['ENGINE']:
            import socket
            import time

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            while sock.connect_ex((db_settings['HOST'], int(db_settings['PORT']))) != 0:
                print("Waiting for database connection...")
                time.sleep(1)

            print("Database connection available")

        super().handle(*args, **options)
