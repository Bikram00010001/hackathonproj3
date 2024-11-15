# Generated by Django 5.0.4 on 2024-05-04 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biopesticide',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Biopesticide id')),
                ('name', models.CharField(max_length=80, verbose_name='Biopesticide Name')),
                ('cost', models.CharField(max_length=80, verbose_name='Cost of Biopersticde')),
            ],
        ),
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Biofertilizer id')),
                ('name', models.CharField(max_length=80, verbose_name='BioFertilizer Name')),
                ('cost', models.CharField(max_length=80, verbose_name='Cost of Fertizers')),
            ],
        ),
        migrations.CreateModel(
            name='Govprice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Gov Price id')),
                ('openprice', models.IntegerField(verbose_name='Gov price')),
            ],
        ),
        migrations.CreateModel(
            name='Herbicide',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Herbicide id')),
                ('name', models.CharField(max_length=80, verbose_name='Herbicide Name')),
                ('cost', models.CharField(max_length=80, verbose_name='Cost of Herbicide')),
            ],
        ),
        migrations.CreateModel(
            name='Openprice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Open Price id')),
                ('openprice', models.IntegerField(verbose_name='Open price')),
            ],
        ),
        migrations.CreateModel(
            name='crop',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='crop id')),
                ('disc', models.CharField(max_length=200, verbose_name='Description')),
                ('name', models.CharField(max_length=80, verbose_name='Crop Name')),
                ('Biopesticide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biopesticide_crops', to='shs.biopesticide', verbose_name='Biopesticide')),
                ('fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fertilizer_crops', to='shs.fertilizer', verbose_name='Fertilizer')),
                ('govprice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='govprice_crops', to='shs.govprice', verbose_name='Govt. Price')),
                ('Herbicide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='herbicide_crops', to='shs.herbicide', verbose_name='Herbicide')),
                ('opencost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opencost_crops', to='shs.openprice', verbose_name='Open Market Price')),
            ],
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='state id')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='State Name')),
                ('crop_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Crops', to='shs.crop')),
            ],
        ),
    ]
