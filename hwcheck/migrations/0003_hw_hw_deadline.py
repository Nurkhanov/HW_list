# Generated by Django 3.2.7 on 2021-11-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwcheck', '0002_course_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hw',
            name='HW_deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
