# Generated by Django 4.2.17 on 2024-12-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_instructor_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
