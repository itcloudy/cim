# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
        ('performance', '0002_auto_20161014_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthrecord',
            options={'ordering': ['-id'], 'verbose_name': '\u6708\u5ea6\u8003\u6838', 'verbose_name_plural': '\u6708\u5ea6\u8003\u6838\u7ba1\u7406'},
        ),
        migrations.AlterField(
            model_name='monthrecord',
            name='date_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
