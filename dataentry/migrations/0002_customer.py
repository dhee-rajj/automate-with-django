# Generated by Django 5.1 on 2024-08-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
