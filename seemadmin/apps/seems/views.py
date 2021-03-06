# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from utils import error, QFRET, success
from .models import Projects, News, Author, Banners


@csrf_protect
@csrf_exempt
def all_pro_info(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)
        ptype = int(request.GET.get('ptype', 0) or 0)
        params = {
            'status': 1
        }
        if ptype:
            params['ptype'] = ptype
        pros = Projects.objects.filter(**params).order_by('-weight', '-create_time').all()
        paginator = Paginator(pros, int(page_size))
        try:
            projects = paginator.page(int(page_num))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            projects = paginator.page(1)
        except EmptyPage:
            projects = []
        if not projects:
            return success({})
        ret = []
        for proj in projects:
            pro_dict = {
                'id': proj.id,
                'title': proj.title,
                'descr': proj.descr,
                'img': proj.img,
                'ptype': proj.ptype,
                'status': proj.status,
                'create_time': proj.create_time,
                'update_time': proj.update_time,
            }
            ret.append(pro_dict)
        return success(ret)


@csrf_protect
@csrf_exempt
def get_project_info(request):
    if request.method == 'GET':
        pid = request.GET.get('pid', 1)
        proj = Projects.objects.filter(id=int(pid), status=1).first()
        pro_dict = {
            'id': proj.id,
            'title': proj.title,
            'descr': render_content_html(proj.descr),
            'img': proj.img,
            'ptype': proj.ptype,
            'status': proj.status,
            'create_time': proj.create_time,
            'update_time': proj.update_time,
        }
        return success(pro_dict)


@csrf_protect
@csrf_exempt
def news_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)
        news_query = News.objects.filter(status=1).order_by('-create_time').all()
        paginator = Paginator(news_query, int(page_size))
        try:
            news_list = paginator.page(int(page_num))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_list = paginator.page(1)
        except EmptyPage:
            news_list = []
        if not news_list:
            return success({})

        ret = []
        for news in news_list:
            news_dict = {
                'id': news.id,
                'title': news.title,
                'content': render_content_html(news.content),
                'img': news.img,
                'status': news.status,
                'create_time': news.create_time,
                'update_time': news.update_time,
            }
            ret.append(news_dict)
        return success(ret)



@csrf_protect
@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.filter(status=1).all()
        ret = []
        for author in authors:
            author_dict = {
                'id': author.id,
                'nickname': author.nickname,
                'english_name': author.english_name,
                'avatar': author.avatar,
                'descr': render_content_html(author.descr),
                'author_type': author.author_type,
                'author_title': '设计师' if author.author_type == 0 else '客户主管',
                'author_eng_title': 'Design' if author.author_type == 0 else 'Client Master',
            }
            ret.append(author_dict)
        return success(ret)


@csrf_protect
@csrf_exempt
def banner_list(request):
    if request.method == 'GET':
        params = {
            'status': 1
        }
        banners = Banners.objects.filter(**params).order_by('-weight', '-create_time').all()

        ret = []
        for b in banners:
            b_dict = {
                'id': b.id,
                'img': b.img,
                'link': b.link or '#',
                'status': b.status,
            }
            ret.append(b_dict)
        return success(ret)


def render_content_html(content):
    parts = content.split('\r\n')
    ret = ""
    for p in parts:
        if p.startswith('http'):
            ret += '<img src="%s" alt="">' % p
        else:
            ret += '<p>%s</p>' % p
    return ret

