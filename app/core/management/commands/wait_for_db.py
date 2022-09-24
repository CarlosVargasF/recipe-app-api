"""
django command to wait for the db to be available1
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

# django throws this error when db is not ready
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to wait for the db"""

    def handle(self, *args, **options):  # fn called when Command is run
        """entrypoint for command"""
        self.stdout.write('waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('db unavailable, waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('db available !! :D'))
