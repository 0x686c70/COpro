# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-02-09 20:13'

from django.conf.urls import url, include

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

urlpatterns = [
    #用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    #用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    #个人中心更改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),

    #发送修改邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    #修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    #我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),

    #收藏机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),
    #收藏讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    #收藏课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),

    #我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),
]
