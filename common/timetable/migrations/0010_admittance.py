# Generated by Django 3.2.12 on 2022-03-28 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20220326_1637'),
        ('timetable', '0009_alter_admittancetype_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admittance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField(null=True, verbose_name='Start Hour')),
                ('end_hour', models.TimeField(null=True, verbose_name='End Hour')),
                ('admittance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminttance_its_type', to='timetable.admittancetype', verbose_name='Admittance Type')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminttance_doctor', to='doctor.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminttance_patient', to='doctor.doctor', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Admittance',
                'verbose_name_plural': 'Admittances',
            },
        ),
    ]
