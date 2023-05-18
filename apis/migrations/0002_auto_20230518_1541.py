# Generated by Django 3.2.18 on 2023-05-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='abstractDesc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='affiliation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='coverage',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='createdDate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='digitalizedDate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='format',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='identifier',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='insertDate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='issuedDate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='medium',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='period',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='publisher',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='reference',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='relation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='subDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='tableOfContents',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='temporal',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='uci',
            field=models.TextField(blank=True),
        ),
    ]