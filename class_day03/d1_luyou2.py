#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/10/21 19:37
@File:  d1_luyou2.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
from flask import Flask

app = Flask(__name__)
app.config["hello"] = "world"


@app.route('/home', redirect_to='/home/test',methods=["GET"])
def home():
    return "sunxy666"


if __name__ == '__main__':
    app.run(debug=True)
