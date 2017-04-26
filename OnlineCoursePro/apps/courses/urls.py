# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-02-01 15:22'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseVideoView, CommentView, AddCommentView, VideoPlayView
urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    #课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),
    #课程
    url(r'^video/(?P<course_id>\d+)$', CourseVideoView.as_view(), name='course_video'),
    #课程评论
    url(r'^comment/(?P<course_id>\d+)$', CommentView.as_view(), name='course_comment'),
    #添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    #视屏播放页面
    url(r'^video_play/(?P<video_id>\d+)$', VideoPlayView.as_view(), name='course_video_play'),
]
