# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='score',
            field=models.FloatField(default=0, verbose_name='\u5f97\u5206'),
        ),
    ]
