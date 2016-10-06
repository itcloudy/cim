# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u8003\u6838\u7ef4\u5ea6')),
                ('mark', models.CharField(max_length=100, null=True, verbose_name='\u5173\u952e\u8bcd', blank=True)),
                ('chief', models.BooleanField(default=False, verbose_name='\u4e0a\u7ea7\u8bc4\u5b9a\u9879')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u8003\u6838\u7ef4\u5ea6',
                'verbose_name_plural': '\u8003\u6838\u7ef4\u5ea6\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='AssessmentLevelGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u7ea7\u522b\u7ec4\u540d\u79f0')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u7ea7\u522b\u7ec4',
                'verbose_name_plural': '\u7ea7\u522b\u7ec4\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='AssessmentLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u8003\u6838\u9879')),
                ('percent', models.FloatField(default=0, verbose_name='\u6743\u91cd')),
                ('key_word', models.CharField(max_length=100, null=True, verbose_name='\u5173\u952e\u8bcd', blank=True)),
                ('prompt', models.CharField(max_length=100, verbose_name='\u8bc4\u4ef7\u5185\u5bb9')),
                ('max_score', models.IntegerField(default=10, verbose_name='\u6700\u9ad8\u5206')),
                ('min_score', models.IntegerField(default=0, verbose_name='\u6700\u4f4e\u5206')),
                ('active', models.BooleanField(default=True, verbose_name='\u6709\u6548')),
                ('assessment', models.ForeignKey(verbose_name='\u8003\u6838\u7ef4\u5ea6', to='performance.Assessment')),
                ('level_group', models.ForeignKey(verbose_name='\u8bc4\u5b9a\u7ea7\u522b\u7ec4', blank=True, to='performance.AssessmentLevelGroup', null=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u8003\u6838\u9879',
                'verbose_name_plural': '\u8003\u6838\u9879\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='AssessmentLineDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', verbose_name='\u5f97\u5206\u6807\u51c6')),
                ('assessment_line', models.ForeignKey(verbose_name='\u8003\u6838\u9879', to='performance.AssessmentLine')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u8003\u6838\u9879\u5206\u7ea7',
                'verbose_name_plural': '\u8003\u6838\u9879\u5206\u7ea7\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='AssessmentLineLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField(default=0, verbose_name='\u5e8f\u53f7')),
                ('name', models.CharField(max_length=50, verbose_name='\u5206\u6570\u7ea7\u522b')),
                ('result', models.CharField(max_length=50, verbose_name='\u7ea7\u522b\u7ed3\u679c')),
                ('max_score', models.FloatField(default=10, verbose_name='\u6700\u9ad8\u5206')),
                ('min_score', models.FloatField(default=0, verbose_name='\u6700\u4f4e\u5206')),
                ('group', models.ForeignKey(verbose_name='\u7ea7\u522b\u7ec4', to='performance.AssessmentLevelGroup')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u7ea7\u522b\u660e\u7ec6',
                'verbose_name_plural': '\u7ea7\u522b\u660e\u7ec6\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('random', models.IntegerField(default=5, verbose_name='\u76f8\u5173\u4eba\u968f\u673a\u6570')),
                ('self_weight', models.FloatField(default=0, null=True, verbose_name='\u81ea\u8bc4\u6743\u91cd', blank=True)),
                ('higher_weight', models.FloatField(default=0, null=True, verbose_name='\u4e0a\u7ea7\u8bc4\u5206\u6743\u91cd', blank=True)),
                ('relevant_weight', models.FloatField(default=0, null=True, verbose_name='\u76f8\u5173\u4eba\u6743\u91cd', blank=True)),
                ('assessment', models.ManyToManyField(to='performance.Assessment', null=True, verbose_name='\u8003\u6838\u7ef4\u5ea6', blank=True)),
                ('department', models.ForeignKey(verbose_name='\u90e8\u95e8', to='base.Department', unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u90e8\u95e8\u8003\u6838\u914d\u7f6e',
                'verbose_name_plural': '\u90e8\u95e8\u8003\u6838\u914d\u7f6e\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='MonthRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('done', models.BooleanField(default=False, verbose_name='\u5b8c\u6210')),
                ('score', models.FloatField(default=-1, verbose_name='\u603b\u5206')),
                ('owner', models.ForeignKey(related_name='month_record_owner', verbose_name='\u5f97\u5206\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6708\u5ea6\u8003\u6838',
                'verbose_name_plural': '\u6708\u5ea6\u8003\u6838\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='MonthScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(default=0, verbose_name='\u5e73\u5747\u5206')),
                ('done', models.BooleanField(default=False, verbose_name='\u5b8c\u6210')),
                ('assessment_line', models.ForeignKey(verbose_name='\u8003\u6838\u9879', blank=True, to='performance.AssessmentLine', null=True)),
                ('month_record', models.ForeignKey(verbose_name='\u8003\u6838\u6708\u4efd', blank=True, to='performance.MonthRecord', null=True)),
                ('owner', models.ForeignKey(related_name='month_score_owner', verbose_name='\u5f97\u5206\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['month_record', 'owner', 'id'],
                'verbose_name': '\u6708\u5ea6\u8003\u6838\u7ed3\u679c',
                'verbose_name_plural': '\u6708\u5ea6\u8003\u6838\u7ed3\u679c\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wait_higher', models.BooleanField(default=False, verbose_name='\u4e0a\u7ea7\u6253\u5206\u9879')),
                ('wait_self', models.BooleanField(default=False, verbose_name='\u81ea\u8bc4\u9879')),
                ('score', models.FloatField(default=-1, verbose_name='\u5f97\u5206')),
                ('date_time', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('mark_time', models.DateTimeField(null=True, verbose_name='\u6253\u5206\u65f6\u95f4', blank=True)),
                ('done', models.BooleanField(default=False, verbose_name='\u5b8c\u6210')),
                ('assessment_line', models.ForeignKey(verbose_name='\u8003\u6838\u9879', to='performance.AssessmentLine')),
                ('mark', models.ForeignKey(related_name='record_mark', verbose_name='\u6253\u5206\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('month_record', models.ForeignKey(verbose_name='\u6708\u4efd', to='performance.MonthRecord')),
                ('owner', models.ForeignKey(related_name='record_owner', verbose_name='\u5f97\u5206\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6253\u5206\u8bb0\u5f55',
                'verbose_name_plural': '\u6253\u5206\u8bb0\u5f55\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('higher', models.ManyToManyField(related_name='higher', null=True, verbose_name='\u9ad8\u7ea7\u76f8\u5173\u4eba', to=settings.AUTH_USER_MODEL, blank=True)),
                ('person', models.ForeignKey(related_name='person', verbose_name='\u62e5\u6709\u8005', to=settings.AUTH_USER_MODEL, unique=True)),
                ('stakeholder', models.ManyToManyField(related_name='stakeholder', null=True, verbose_name='\u666e\u901a\u76f8\u5173\u4eba', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '\u76f8\u5173\u4eba',
                'verbose_name_plural': '\u76f8\u5173\u4eba\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='assessmentlinedetail',
            name='level',
            field=models.ForeignKey(verbose_name='\u8bc4\u5b9a\u7ea7\u522b', blank=True, to='performance.AssessmentLineLevel', null=True),
        ),
        migrations.AddField(
            model_name='assessmentlinedetail',
            name='level_group',
            field=models.ForeignKey(verbose_name='\u8bc4\u5b9a\u7ea7\u522b\u7ec4', blank=True, to='performance.AssessmentLevelGroup', null=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='level_group',
            field=models.ForeignKey(verbose_name='\u8bc4\u5b9a\u7ea7\u522b\u7ec4', blank=True, to='performance.AssessmentLevelGroup', null=True),
        ),
    ]
