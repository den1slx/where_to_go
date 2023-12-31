# Generated by Django 4.2.4 on 2023-08-30 08:22

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_fix_verbose_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'Images'},
        ),
        migrations.RemoveField(
            model_name='placeimage',
            name='my_order',
        ),
        migrations.AddField(
            model_name='placeimage',
            name='ordering',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Упорядочение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(default='', verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место'),
        ),
    ]
