# Generated by Django 2.2.2 on 2019-06-13 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('number', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='app/')),
            ],
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_process', models.IntegerField(default=1)),
                ('date', models.CharField(max_length=64)),
                ('time', models.TimeField()),
                ('who_call', models.CharField(max_length=64)),
                ('how_long', models.CharField(default=1, max_length=128)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone_numbers.Names')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
            },
        ),
    ]