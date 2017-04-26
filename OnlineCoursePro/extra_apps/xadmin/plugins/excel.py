# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-02-20 21:01'
from django.template import loader
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView


class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', ))

