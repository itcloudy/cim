# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(null=True, default=b'', max_length=20, blank=True, unique=True, verbose_name='\u7535\u8bdd')),
                ('short_phone', models.CharField(default=b'', max_length=10, null=True, verbose_name='\u77ed\u53f7', blank=True)),
                ('username_zh', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u4e2d\u6587\u540d\u79f0', blank=True)),
                ('chief', models.ForeignKey(verbose_name='\u4e0a\u7ea7', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u90e8\u95e8')),
                ('charge', models.ForeignKey(related_name='charge', verbose_name='\u8d1f\u8d23\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(verbose_name='\u4e0a\u7ea7\u90e8\u95e8', blank=True, to='base.Department', null=True)),
            ],
            options={
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u804c\u4f4d')),
                ('description', models.TextField(null=True, verbose_name='\u804c\u8d23\u8bf4\u660e', blank=True)),
                ('requirements', models.TextField(null=True, verbose_name='\u5c97\u4f4d\u8981\u6c42', blank=True)),
            ],
            options={
                'verbose_name': '\u804c\u4f4d',
                'verbose_name_plural': '\u804c\u4f4d\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u56e2\u961f\u540d\u79f0')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u56e2\u961f\u6709\u6548')),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u56e2\u961f\u6210\u5458')),
            ],
            options={
                'verbose_name': '\u56e2\u961f',
                'verbose_name_plural': '\u56e2\u961f\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(verbose_name='\u90e8\u95e8', blank=True, to='base.Department', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ForeignKey(verbose_name='\u804c\u4f4d', blank=True, to='base.Position', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
