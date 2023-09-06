import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Restore the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "database_type",
            type=str,
            help="Indicates the type of the database (e.g., postgres, sqlite, mysql)",
        )
        parser.add_argument(
            "backup_location", type=str, help="The location of the backup file"
        )

    def handle(self, *args, **kwargs):
        database_type = kwargs["database_type"]
        backup_location = kwargs["backup_location"]

        if database_type == "postgres":
            subprocess.run(["pg_restore", "-d", "mydatabase", backup_location])
        elif database_type == "sqlite":
            db_path = settings.DATABASES["default"]["NAME"]
            subprocess.run(["sqlite3", db_path, f".restore {backup_location}"])
        elif database_type == "mysql":
            subprocess.run(["mysql", "mydatabase", "<", backup_location])
        else:
            self.stdout.write(self.style.ERROR("Unknown database type"))
