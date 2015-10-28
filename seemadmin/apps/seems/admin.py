# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Projects, Author, News, CdnMedia
from .forms import AuthorAdminForm
import time
from utils import qiniu_upload
import copy


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['status']
    search_fields = ['nickname']
    list_display = ('id', 'nickname', 'english_name', 'status', 'create_time', 'update_time')

    form = AuthorAdminForm


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['title', 'descr']
    list_display = ('id', 'title', 'descr', 'img', 'ptype', 'status', 'create_time', 'update_time')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['title', 'content']
    list_display = ('id', 'title', 'content', 'img', 'status', 'create_time', 'update_time')



@admin.register(CdnMedia)
class CdnMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_size', 'display_img', 'supplier', 'url', 'remark',
                    'create_time']

    search_fields = ['remark']

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        # return False
        return True

    def add_view(self, request, form_url='', extra_context=None):
        self.fields = ['image', 'supplier', 'remark']
        self.readonly_fields = []
        return super(CdnMediaAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.fields = ['id', 'display_size', 'display_img', 'supplier', 'url', 'remark',
                       'create_time', 'update_time']
        self.readonly_fields = copy.deepcopy(self.fields)
        self.readonly_fields.remove('remark')
        return super(CdnMediaAdmin, self).change_view(request, object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        if not change:  # 仅在新建时上传图片
            try:
                # import pdb
                # pdb.set_trace()
                name_suffix = obj.image.name.split('.')[-1]
                save_path = 'op_upload/{op_id}/{name}.{suffix}'. \
                    format(op_id=int(request.user.id),
                           name=str(time.time()).replace('.', ''),
                           suffix=name_suffix)
                obj.url = qiniu_upload(obj.image.read(), 'seemtest', save_path)
                try:  # 防止不能识别的文件格式导致 pillow 的 decoder error
                    obj.width = obj.image.width
                    obj.height = obj.image.height
                except:
                    pass
                obj.image = None  # 不要保存
            except Exception as e:
                print e
                return
        return super(CdnMediaAdmin, self).save_model(request, obj, form, change)

