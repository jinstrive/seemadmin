# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.seems.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nickname', models.CharField(max_length=20, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe5\x90\x8d\xe7\xa7\xb0')),
                ('english_name', models.CharField(max_length=50, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d')),
                ('author_type', models.IntegerField(default=0, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe8\xae\xbe\xe8\xae\xa1\xe5\xb8\x88\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x97\xa0\xe6\x95\x88'), (1, b'\xe6\x9c\x89\xe6\x95\x88')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'author',
                'verbose_name': '\u4f5c\u8005\u4fe1\u606f',
                'verbose_name_plural': '\u4f5c\u8005\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='CdnMedia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to=apps.seems.models.path_gen, max_length=255, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xbf\x9d\xe5\xad\x98\xe8\xb7\xaf\xe5\xbe\x84')),
                ('width', models.SmallIntegerField(null=True, verbose_name=b'\xe5\xae\xbd\xe5\xba\xa6', blank=True)),
                ('height', models.SmallIntegerField(null=True, verbose_name=b'\xe9\xab\x98\xe5\xba\xa6', blank=True)),
                ('supplier', models.SmallIntegerField(default=1, verbose_name=b'cdn \xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86', choices=[(1, b'\xe4\xb8\x83\xe7\x89\x9b')])),
                ('url', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80')),
                ('remark', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'cdn_image',
                'verbose_name': '\u4e0a\u4f20\u56fe\u7247',
                'verbose_name_plural': '\u4e0a\u4f20\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('content', models.CharField(max_length=5000, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x86\x85\xe5\xae\xb9')),
                ('img', models.CharField(max_length=200, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\xa4\xb4\xe5\x9b\xbe')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x97\xa0\xe6\x95\x88'), (1, b'\xe6\x9c\x89\xe6\x95\x88')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news',
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('descr', models.CharField(max_length=5000, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x86\x85\xe5\xae\xb9')),
                ('img', models.CharField(max_length=200, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\xa4\xb4\xe5\x9b\xbe')),
                ('ptype', models.IntegerField(default=1, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'logo'), (2, b'vi'), (3, b'app'), (4, b'web')])),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe8\xae\xbe\xe8\xae\xa1\xe5\xb8\x88\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x97\xa0\xe6\x95\x88'), (1, b'\xe6\x9c\x89\xe6\x95\x88')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'projects',
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
        ),
    ]
