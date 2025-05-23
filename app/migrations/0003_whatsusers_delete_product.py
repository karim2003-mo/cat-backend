# Generated by Django 5.1.6 on 2025-03-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_delete_design'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('latestmessage', models.TextField()),
                ('lastchattime', models.DateTimeField()),
                ('unreadedmessages', models.IntegerField(max_length=4)),
                ('image', models.ImageField(upload_to='users_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
