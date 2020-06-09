import os

from flask import Flask, request, render_template, redirect

from Api.getyaml.json_to_yaml import json_to_yaml, make_locustfile, make_apifile
from Api.public.WriteJson import write_json
from Api.settings import CASE_DIR
from Api.public.do_command import cmd

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # 获取表单内容
        name = request.form.get('name')
        if request.form.get('isauto'):  # 判断是否勾选自动填写
            name = '%auto'
        url = request.form.get('url')
        meth = request.form.get('meth')
        remark = request.form.get('remark')
        json_data = request.form.get('json_data')
        menu = request.form.get('menu')

        # 写入json文件
        write_json(json_data=json_data)

        # yaml输出路径
        case_path = os.path.join(CASE_DIR, name) + '.yaml'

        # 执行操作
        if menu == '1':
            a = json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
            b = make_locustfile(name=name, remark=remark)
            c = make_apifile(name=name, remark=remark)
            msg = a + b + c
            print(msg)
            context = {
                'msg': msg
            }
            return render_template('index.html',**context)



if __name__ == '__main__':
    app.run(debug=True)
