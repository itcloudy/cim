# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0005_auto_20161015_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthrecord',
            name='score',
            field=models.FloatField(default=0, verbose_name='\u603b\u5206'),
        ),
    ]
