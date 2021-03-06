# Generated by Django 2.0.7 on 2018-07-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='heatidx',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='measurement',
            name='humidity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='measurement date'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(default=0),
        ),
    ]
