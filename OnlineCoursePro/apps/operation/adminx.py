# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-01-23 13:51'

import xadmin

from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
