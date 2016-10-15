# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=20, verbose_name='\u90e8\u95e8\u6708\u4efd\u8003\u6838', blank=True)),
                ('department', models.ForeignKey(related_name='month_department', verbose_name='\u90e8\u95e8', to='base.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ResultCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.ManyToManyField(related_name='check_department', verbose_name='\u90e8\u95e8', to='base.Department')),
                ('user', models.ForeignKey(related_name='check_user', verbose_name='\u67e5\u770b\u4eba', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': '\u7ed3\u679c\u67e5\u770b',
                'verbose_name_plural': '\u7ed3\u679c\u67e5\u770b\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='monthrecord',
            name='date_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='record',
            name='score',
            field=models.FloatField(default=0, verbose_name='\u5f97\u5206'),
        ),
    ]
