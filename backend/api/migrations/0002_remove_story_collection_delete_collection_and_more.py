# Generated by Django 4.2.3 on 2023-08-09 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
