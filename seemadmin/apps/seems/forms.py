# -*- coding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE


class AuthorAdminForm(forms.ModelForm):

    descr = forms.CharField(label='作者简介', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

