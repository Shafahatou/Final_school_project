# Generated by Django 4.2.17 on 2024-12-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_alter_chapitre_id_alter_classe_id_alter_cours_id_and_more'),
        ('instructor', '0006_alter_instructor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='matieres',
            field=models.ManyToManyField(blank=True, related_name='instructors', to='school.matiere'),
        ),
    ]
