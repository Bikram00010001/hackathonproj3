# Generated by Django 5.0.4 on 2024-05-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shs', '0004_alter_crop_biopesticide_alter_crop_fertilizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='states',
            name='crop_id',
        ),
        migrations.AddField(
            model_name='states',
            name='crop_id',
            field=models.ManyToManyField(to='shs.crop'),
        ),
    ]
