#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/10/21 11:59
@File:  d2_flask_abc.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
from flask import Flask, request,render_template

# request，保存你请求数据
# 初始化application
app = Flask(__name__,
            template_folder="test_folder"
            )


# 添加路由
@app.route("/")
def index():
    args = request.args
    print(args.get(()))
    return render_template("index.html")


# 运行服务器
app.run(port=5000)
