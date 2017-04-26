# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-01-24 17:34'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from OnlineCoursePro.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(6)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '您的CourseOnline激活注册连接'
        email_body = '请点击以下连接激活帐号: http://127.0.0.1:8000/active/%s' % code
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '您的CourseOnline密码重置链接'
        email_body = '请点击以下链接进行重置密码: http://127.0.0.1:8000/reset/%s -- 请勿转发他人' % code
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = 'CourseOnline邮箱修改验证码'
        email_body = '你的邮箱验证码为：%s -- 请勿转发他人' % code
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
