# -*- coding:utf-8 -*-
__author__ = 'WdAxz'
__date__ = '2017-01-23 16:48'

from django import forms

from .models import UserProfile

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30, min_length=5)
    password = forms.CharField(required=True, max_length=32, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=32, min_length=6)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birthday', 'gender', 'mobile', 'address']
