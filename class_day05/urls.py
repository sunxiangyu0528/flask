#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/11/4 18:01
@File:  urls.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
from class_day05 import views
from class_day05.d1_app_route import app

app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/index', view_func=views.index)
