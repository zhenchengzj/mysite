#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# @Author    :韶华舞流年
# @Time      :2020/9/29 18:59
# @Desc      :

from django.urls import path
from . import _views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', _views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', _views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', _views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', _views.vote, name='vote'),
]
