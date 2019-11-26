from flask import Flask, request, render_template,send_from_directory, make_response
from Archives import Archives
import pickle,base64,os
from jinja2 import Environment
from random import choice
import numpy
import builtins
import io
import re

app = Flask(__name__)
Jinja2 = Environment()
def set_str(type,str):
    retstr = "%s'%s'"%(type,str)
    print(retstr)
    return eval(retstr)
def get_cookie():
    check_format = ['class','+','getitem','request','args','subclasses','builtins','{','}']
    return choice(check_format)

@app.route('/')
def index():
    global Archives
    resp = make_response(render_template('index.html', Archives = Archives))
    cookies = bytes(get_cookie(), encoding = "utf-8")
    value = base64.b64encode(cookies)
    resp.set_cookie("username", value=value)
    return resp

@app.route('/Archive/<int:id>')
def Archive(id):
    global Archives
    if id>len(Archives):
        return render_template('message.html', msg='文章ID不存在！', status='失败')
    return render_template('Archive.html',Archive = Archives[id])

@app.route('/message',methods=['POST','GET'])
def message():
    if request.method == 'GET':
        return render_template('message.html')
    else:
        type = request.form['type'][:1]
        msg = request.form['msg']
        try:
            info = base64.b64decode(request.cookies.get('user'))
            info = pickle.loads(info)
            username = info["name"]
        except Exception as e:
            print(e)
            username = "Guest"

        if len(msg)>27:
            return render_template('message.html', msg='留言太长了！', status='留言失败')
        msg = msg.replace(' ','')
        msg = msg.replace('_', '')
        retstr = set_str(type,msg)
        return render_template('message.html',msg=retstr,status='%s,留言成功'%username)

@app.route('/hello',methods=['GET', 'POST'])
def hello():
    username = request.cookies.get('username')
    username = str(base64.b64decode(username), encoding = "utf-8")
    data = Jinja2.from_string("Hello , " + username + '!').render()
    is_value = False
    return render_template('hello.html', msg=data,is_value=is_value)


@app.route('/getvdot',methods=['POST','GET'])
def getvdot():
    if request.remote_addr != "10.10.0.2":
        return "345"
    if request.method == 'GET':
        return render_template('getvdot.html')
    else:
        matrix1 = base64.b64decode(request.form['matrix1'])
        matrix2 = base64.b64decode(request.form['matrix2'])
        try:
            matrix1 = numpy.loads(matrix1)
            matrix2 = numpy.loads(matrix2)
        except Exception as e:
            print(e)
        result = numpy.vdot(matrix1,matrix2)
        print(result)
        return render_template('getvdot.html',msg=result,status='向量点积')


@app.route('/robots.txt',methods=['GET'])
def texts():
    return send_from_directory('/', 'flag', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)
