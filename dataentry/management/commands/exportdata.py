from django.core.management.base import BaseCommand
from django.apps import apps
import datetime
import csv

class Command(BaseCommand):
    help = "Export data from a modle into csv file"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="model_name to export")

    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"].capitalize()
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = f"exported_{model_name}_data_{timestamp}"

        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        if not model:
            self.stderr.write(f"Model:{model_name} not found")
            return

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([field.name for field in model._meta.fields])
            data = model.objects.all()
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])


        self.stdout.write(self.style.SUCCESS("Exported data successfully into CSV file"))



