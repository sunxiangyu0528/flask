#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/10/21 11:59
@File:  d2_flask_abc.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
from flask import Flask, request, render_template

# request，保存你请求数据
# 1、初始化application,--name--表示flask初始化app对象的名字，通过名字得到app现在的位置
app = Flask(__name__,
            template_folder="test_folder"
            )


# 2.添加路由，view function
@app.route("/")
def index():
    args = request.args
    print(args.get(()))
    return render_template("index.html")


# 3.运行服务器
# 调试，测试，开发，自带，不要用于生产环境
# __name__好处，
if __name__ == "__main__":
    app.run()
