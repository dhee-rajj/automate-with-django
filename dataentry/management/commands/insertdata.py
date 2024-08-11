from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "To insert data into database"

    def handle(self, *args, **kwargs):
        dataset = [{"roll_no": 8023, "name": "Dheeraj", "age": 22},
                   {"roll_no": 8024, "name": "Rohit", "age": 37},
                   {"roll_no": 8025, "name": "Kohli", "age": 36}, 
                   {"roll_no": 8024, "name": "King", "age": 40}]

        for data in dataset:
            roll_no = data["roll_no"]
            exists = Student.objects.filter(roll_no=roll_no).exists()

            if not exists:
                Student.objects.create(
                    roll_no=data["roll_no"], name=data["name"], age=data["age"])
            else:
                self.stdout.write(self.style.WARNING(
                    f"provided data(roll_no):{roll_no} already exists"))
        self.stdout.write(self.style.SUCCESS("Inserted data successfully"))
