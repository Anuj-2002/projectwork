# Generated by Django 3.2.12 on 2022-03-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_names', models.TextField(verbose_name='Full Names ')),
                ('message', models.TextField(verbose_name='Description ')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
