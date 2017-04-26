# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-01-23 13:41'

import xadmin

from .models import CourseOrg, Teacher, CityDict


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums', 'add']
    # relfield_style = 'fk-ajax'


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'add']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'add']
    relfield_style = 'fk-ajax'

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
