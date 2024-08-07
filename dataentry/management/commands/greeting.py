from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays a greeting with the name specified'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="For username")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f"Hi {name}, Great to meet"
        self.stdout.write(self.style.SUCCESS(greeting))