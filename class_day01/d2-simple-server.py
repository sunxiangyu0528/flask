#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/9/24 19:18
@File:  d2-simple-server.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
# 搭建服务
# 监听动作 while  0.1s
# 处理程序  application
# 返回数据到套节字，生成一个响应对象

from wsgiref.simple_server import make_server


def app(env, start_response):
    start_response("200 ok", [("content-type", "text/plain")])
    return [b"{hello,sunxy}"]


server = make_server("", 6001, app=app)
server.serve_forever()
