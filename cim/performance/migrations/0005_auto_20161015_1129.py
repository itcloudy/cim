# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0004_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthperformance',
            options={'ordering': ['-id'], 'verbose_name': '\u6708\u4efd', 'verbose_name_plural': '\u6708\u4efd\u7ba1\u7406'},
        ),
    ]
