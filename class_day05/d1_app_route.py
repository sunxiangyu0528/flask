#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/11/4 17:31
@File:  d1_app_route.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
# @app.route和app.add_url_rule参数：
#
# 1 rule,URL规则
# 3 view_func, 视图函数名称
# 5 defaults=None, 默认值,当URL中无参数，函数需要参数时，使用 defaults={'k':'v'}为函数提供参数
# 7 endpoint=None, 名称，用于反向生成URL，即： url_for('名称')
# 9 methods=None, 允许的请求方式，如：["GET","POST"]
# strict_slashes=None,对URL最后的 / 符号是否严格要求


# 路由单个注册，集中注册
# app.add_url_rule
from flask import Flask

app = Flask(__name__)
from class_day05.urls import *
from class_day05 import urls

# app.add_url_rule('/', view_func="里面导入视图函数")


# @app.route('/home', redirect_to='/home/test', methods=["GET"])
# def home():
#     return "sunxy666"


if __name__ == '__main__':
    app.run(debug=True)
