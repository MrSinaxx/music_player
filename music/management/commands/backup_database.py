import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Back up the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "database_type",
            type=str,
            help="Indicates the type of the database (e.g., postgres, sqlite, mysql)",
        )
        parser.add_argument(
            "backup_location",
            type=str,
            help="The location where the backup will be saved",
        )

    def handle(self, *args, **kwargs):
        database_type = kwargs["database_type"]
        backup_location = kwargs["backup_location"]

        if database_type == "postgres":
            subprocess.run(["pg_dump", "mydatabase", "-f", backup_location])
        elif database_type == "sqlite":
            subprocess.run(
                ["sqlite3", "mydatabase", f".backup {backup_location}/backup.sqlite"]
            )
        elif database_type == "mysql":
            subprocess.run(["mysqldump", "mydatabase", "-r", backup_location])
        else:
            self.stdout.write(self.style.ERROR("Unknown database type"))
