# Generated by Django 4.0.3 on 2022-04-08 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0018_alter_admittancetype_color_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admittancetype',
            old_name='color_class',
            new_name='color',
        ),
    ]
