# Generated by Django 3.2.7 on 2021-10-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwcheck', '0003_alter_hw_hw_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hw',
            name='hw_number',
        ),
        migrations.AddField(
            model_name='hw',
            name='hw_info',
            field=models.CharField(default='Not NULL', max_length=255),
            preserve_default=False,
        ),
    ]
