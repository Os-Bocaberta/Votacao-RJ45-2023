# Generated by Django 4.2.2 on 2023-06-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_candidates_path_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voters',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
