# -*- coding:utf-8 -*-
from django.db import models
import datetime

STATUS_CHOICES = (
    (0, '无效'),
    (1, '有效'),
)

class Author(models.Model):

    TYPE_CHOICES = (
        (0, '设计师'),
        (1, '客户主管'),
    )

    id = models.AutoField(primary_key=True)
    nickname = models.CharField('作者名称', max_length=20)
    english_name = models.CharField('英文名', max_length=50)
    descr = models.TextField('作者简介', max_length=5000)
    # descr = HTMLField('作者简介', max_length=5000)
    avatar = models.CharField('作者头像', max_length=500)
    author_type = models.IntegerField('作者类型', choices=TYPE_CHOICES, default=0)
    status = models.IntegerField('设计师状态', choices=STATUS_CHOICES, default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者信息'
        verbose_name_plural = verbose_name


class Projects(models.Model):

    PTYPE_CHOICES = (
        (1, 'logo'),
        (2, 'vi'),
        (3, 'app'),
        (4, 'web'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField('项目名称', max_length=50)
    descr = models.TextField('项目内容', max_length=5000)
    img = models.CharField('项目头图', max_length=200)
    ptype = models.IntegerField('项目类型', choices=PTYPE_CHOICES, default=1)
    status = models.IntegerField('项目状态', choices=STATUS_CHOICES, default=1)
    weight = models.IntegerField('项目权重', default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects'
        verbose_name = '项目'
        verbose_name_plural = verbose_name


class News(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField('新闻名称', max_length=50)
    content = models.TextField('新闻内容', max_length=5000)
    img = models.CharField('新闻头图', max_length=200)
    status = models.IntegerField('新闻状态', choices=STATUS_CHOICES, default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'news'
        verbose_name = '新闻'
        verbose_name_plural = verbose_name


def path_gen(instance, filename):
    create_time = datetime.datetime.now()
    return 'seem/op_upload/{date}/{day}/{filename}'. \
        format(date=create_time.strftime('%Y-%m'),
               day=create_time.strftime('%d'),
               filename=filename)


class CdnMedia(models.Model):
    """手工上传图片"""
    TYPE_CHOICES = (
        (1, '图片'),
    )

    CDN_CHOICES = (
        (1, '七牛'),
    )

    def display_img(self, width=77):
        return '<img src="{url}" height="{height}", width="{width}", onclick="window.open(this.src)"/>'. \
            format(url=self.url,
                   width=width,
                   height=width*self.height/self.width if self.width and self.height else width)

    display_img.short_description = '图片预览'
    display_img.allow_tags = True

    def display_size(self):
        if self.width and self.height:
            return '{width} * {height}'.format(width=self.width, height=self.height)
        else:
            return '未知'

    display_size.short_description = '图片尺寸'

    id = models.AutoField(primary_key=True)
    image = models.ImageField('图片保存路径', upload_to=path_gen, max_length=255)
    width = models.SmallIntegerField('宽度', blank=True, null=True)
    height = models.SmallIntegerField('高度', blank=True, null=True)
    supplier = models.SmallIntegerField('cdn 服务商', choices=CDN_CHOICES, default=1)
    url = models.CharField('图片地址', max_length=255)
    remark = models.CharField('备注', max_length=255, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'cdn_image'
        verbose_name = '上传图片'
        verbose_name_plural = verbose_name