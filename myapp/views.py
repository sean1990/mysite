# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(req):
    name = '你好欢迎访问'
    return render(req,'index.html',locals())