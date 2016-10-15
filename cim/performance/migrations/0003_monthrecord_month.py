# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20161014_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthrecord',
            name='month',
            field=models.ForeignKey(default=1, verbose_name='\u6708\u4efd', to='performance.MonthPerformance'),
            preserve_default=False,
        ),
    ]
