# Generated by Django 4.0.4 on 2023-04-28 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cerebrum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='find_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 11, 46, 56, 613178)),
            preserve_default=False,
        ),
    ]
