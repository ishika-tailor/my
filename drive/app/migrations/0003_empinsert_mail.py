# Generated by Django 3.0.6 on 2020-06-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_empinsert_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='empinsert',
            name='mail',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
