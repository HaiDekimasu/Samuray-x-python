# Generated by Django 5.0 on 2024-01-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capitulos', '0003_alter_capitulos_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulos',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
