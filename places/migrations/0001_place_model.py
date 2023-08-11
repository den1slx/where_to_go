# Generated by Django 3.2.19 on 2023-08-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description_short', models.CharField(max_length=350, null=True, verbose_name='краткое описание')),
                ('description_long', models.TextField(null=True, verbose_name='Описание')),
                ('lng', models.FloatField(null=True, verbose_name='longitude')),
                ('lat', models.FloatField(null=True, verbose_name='latitude')),
                ('imgs', models.TextField(null=True)),
            ],
        ),
    ]