# Generated by Django 5.0.6 on 2024-06-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('collage_no', models.IntegerField()),
                ('city', models.CharField(max_length=120)),
                ('iet_no', models.IntegerField(max_length=50)),
            ],
        ),
    ]
