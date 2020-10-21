#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/10/19 21:39
@File:  d1_luyou.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
# 尝试编辑
# 定义三个url，'/'首页，'/login'登陆，'projects'项目
# 对三个url做出响应，繁简由人
# 如果不存在，报404错误
from wsgiref.simple_server import make_server


def home():
    return "hello"


def login():
    return "login"


def projects():
    return "projects"


# url和处理程序绑定在一起，叫做路由
patterns = {
    "/": home,
    "/login": login,
    "/projects": projects
}


def app(env, start_response):
    """
    如果出现了很多分支都是==，字典去封装
    :param env:
    :param start_response:
    :return:
    """
    url = env.get("PATH_INFO")
    if (url not in patterns.keys()) or url is None:
        start_response("404 not found", [("content-type", "text/plain")])
        return [b"page not found"]
    start_response("200 ok", [("content-type", "text/plain")])

    resp = patterns.get(url)
    if resp is None:
        start_response("404 not found", [("content-type", "text/plain")])
        return [b"page not found"]
    return [resp().encode()]


server = make_server("", 6001, app=app)
server.serve_forever()
# else :
#     start_response("200 ok", [("content-type", "text/plain")])
#     return [b"{}".f]


# if env.get("PATH_INFO") == "/":
#     start_response("200 ok", [("content-type", "text/plain")])
#     res = home()
#     return [res.encode()]
# elif env.get("PATH_INFO") == "/login":
#     start_response("200 ok", [("content-type", "text/plain")])
#     res = login()
#     return [res.encode()]
# elif env.get("PATH_INFO") == "/projects":
#     start_response("200 ok", [("content-type", "text/plain")])
#     res = login()
#     return [res.encode()]
# else:
#     start_response("404 ok", [("content-type", "text/plain")])
#     return [b"page not found"]
