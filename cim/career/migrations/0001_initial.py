# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u95ee\u9898\u7b54\u6848')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='\u95ee\u9898')),
                ('key_word', models.TextField(verbose_name='\u5173\u952e\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898\u7ba1\u7406',
            },
        ),
    ]
