# -*- encoding: utf-8 -*-

from  django.apps import AppConfig

class baseConfig(AppConfig):
    name ='base'
    verbose_name = u'基础信息管理'

    def ready(self):
        import base.signals