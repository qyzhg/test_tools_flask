import os

from flask import Flask, request, render_template, redirect,url_for

from Api.getyaml.json_to_yaml import json_to_yaml, make_locustfile, make_apifile
from Api.public.WriteJson import write_json
from Api.settings import CASE_DIR,HOST

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # 获取表单内容
        url = request.form.get('url')
        if HOST in url:
            url = url.split(HOST)[1]
        meth = request.form.get('meth')
        name = request.form.get('name')
        if request.form.get('isauto'):  # 判断是否勾选自动填写
            name = name = (url + '_' + meth.upper()).replace('/', '_')
        remark = request.form.get('remark')
        json_data = request.form.get('json_data')
        menu = request.form.get('menu')
        # 写入json文件
        write_json(json_data=json_data)
        # yaml输出路径
        case_path = os.path.join(CASE_DIR, name) + '.yaml'
        # 执行操作
        msg = list()
        warning = list()
        a = json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
        msg.append(a)
        if menu == '1':
            b = make_locustfile(name=name, remark=remark)
            msg.append(b)
            c = make_apifile(name=name, remark=remark)
            msg.append(c)
        if menu == '2':
            b = make_locustfile(name=name, remark=remark)
            msg.append(b)
        if menu == '3':
            c = make_apifile(name=name, remark=remark)
            msg.append(c)
        context = {
            'msg': msg,
            'warning':warning,
        }
        return render_template('index.html', **context)


@app.route('/start',methods=['POST','GET'])
def start():
    pass



if __name__ == '__main__':
    app.run(debug=True)
