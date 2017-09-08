# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(req,'polls/index.html', locals())

def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('没找着：）')
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', locals())

def results(req, question_id):
    response = "您正在看问题的结果 %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("您正在投票 %s." % question_id)