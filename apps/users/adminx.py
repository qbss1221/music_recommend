# -*- coding: utf-8 -*-
__author__ = 'qbss'
__date__ = '2018/4/1 14:29'

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)