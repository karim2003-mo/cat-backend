# Generated by Django 5.1.6 on 2025-02-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designername', models.CharField(max_length=100)),
                ('designerexp', models.IntegerField()),
                ('designtype', models.CharField(max_length=100)),
                ('designrate', models.FloatField()),
                ('designsubrate', models.IntegerField()),
                ('designimages', models.TextField()),
            ],
        ),
    ]
