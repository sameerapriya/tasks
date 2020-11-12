# Generated by Django 3.0.8 on 2020-11-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('task_from', models.DateTimeField()),
                ('task_to', models.DateTimeField()),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]