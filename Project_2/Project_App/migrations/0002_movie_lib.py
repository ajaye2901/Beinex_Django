# Generated by Django 5.0.3 on 2024-03-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Lib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Lib_ID', models.IntegerField()),
            ],
        ),
    ]
