# Generated by Django 3.0.7 on 2020-06-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=300, null=True)),
                ('area_de_interesse', models.CharField(blank=True, max_length=300, null=True)),
                ('nome_camera', models.CharField(blank=True, max_length=300, null=True)),
                ('localizacao_fisica', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Camera',
                'verbose_name_plural': 'Cameras',
            },
        ),
    ]
