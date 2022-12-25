# Generated by Django 4.1 on 2022-11-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutoring", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="grade_level",
            field=models.CharField(
                choices=[
                    ("FR", "Freshman - (9th Grade)"),
                    ("SO", "Sophomore - (10th Grade)"),
                    ("JR", "Junior - (11th Grade)"),
                    ("SR", "Senior - (12th Grade)"),
                    ("GR", "University"),
                ],
                default="JR",
                max_length=2,
                verbose_name="Grade Level",
            ),
        ),
    ]
