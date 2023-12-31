# Generated by Django 4.1.6 on 2023-02-07 13:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('number_of_pages', models.IntegerField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
