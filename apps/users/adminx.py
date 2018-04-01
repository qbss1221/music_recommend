# -*- coding: utf-8 -*-
__author__ = 'huxixi'
__date__ = '2018/4/1 14:29'

import xadmin

from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 列表展示
    search_fields = ['code', 'email', 'send_type']  # 搜索字段
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 过滤器


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)