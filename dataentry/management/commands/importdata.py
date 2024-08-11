from django.core.management.base import BaseCommand,CommandError
from django.apps import apps
import csv


class Command(BaseCommand):
    help = "To import data from a CSV file for provided modle"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="CSV file path")
        parser.add_argument("model_name", type=str, help="model_name to import")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"].capitalize()
        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f"Model:{model_name} not found in any app")

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Imported data successfully from CSV file"))
