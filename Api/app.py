from flask import Flask, request, render_template, redirect
from Api.public.WriteJson import write_json
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
        # 写入json文件
        write_json(json_data=json_data)
        # 执行操作
        # a = cmd(name=name, url=url, meth=meth, remark=remark)
        context = {
            'msg': 'test'
        }
        return redirect('menu')


@app.route('/menu',methods=['POST','GET'])
def menu():
    if request.method == 'GET':
        return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
