# Generated by Django 5.0.4 on 2024-04-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('History', '0002_alter_history_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='historyarr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='history',
            name='winrate',
            field=models.FloatField(default=0, max_length=3),
        ),
    ]
