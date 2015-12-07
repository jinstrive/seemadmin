#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

# 商品库
urlpatterns = patterns(
    'apps.seems.views',
    url(r'^all_pro_info$', 'all_pro_info'),  # 获取项目列表
    url(r'^project_detail$', 'get_project_info'),  # 获取项目列表
    url(r'^all_news_info$', 'news_list'),  # 获取新闻列表
    url(r'^all_authors$', 'author_list'),  # 获取新闻列表
    url(r'^banners$', 'banner_list'),  # 获取banner列表
)
