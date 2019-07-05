from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, make_response, flash, render_template_string
from database import session, User, Blog
from scripts import *
import hashlib
import os


app = Flask(__name__)
app.secret_key = '123456'
COOKIE_KEY = 'key'
_site_name = '杨超越粉丝后援会'


def login_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		username = cookie_to_username(request.cookies.get(COOKIE_KEY, ''))
		if username is '' or len(session.query(User).filter(User.username == username).all()) is 0:
			flash('请先登录!')
			return redirect(url_for('signin'))
		kwargs['username'] = username
		return func(*args, **kwargs)
	return wrapper

@app.route('/')
def _():
	return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		username = request.form.get('username', '')
		password = request.form.get('password', '')
		if username == 'admin':
			flash('注册失败。该用户已存在')
			return redirect(url_for('signup'))
		if is_username_legal(username) == False:
			flash('注册失败。用户名必须为6位以上的英文字母或数字')
			return redirect(url_for('signup'))
		if is_password_legal(password) == False:
			flash('注册失败。密码必须为6位以上的英文字母或数字')
			return redirect(url_for('signup'))
		if is_username_legal(username) and is_password_legal(password):
			if len(session.query(User).filter(User.username == username).all()) is 0:
				session.add(User(username=username, password=hash_password(password)))
				flash('注册成功!')
				return redirect(url_for('signin'))
			else:
				flash('注册失败。用户名已存在')
				return redirect(url_for('signup'))
		flash('注册失败')
		return redirect(url_for('signup'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		return render_template('signin.html')
	else:
		username = request.form.get('username', '')
		password = request.form.get('password', '')
		if '' not in (username, password):
			users = session.query(User).filter(User.username == username).all()
			if len(users) is 1:
				user = users[0]
				if user.password == hash_password(password):
					try:
						if user.username == 'admin':
							string = '管理员权限用户 admin 登录成功!欢迎来到{}!<br><a href="/blogs">点击进入首页</a>'.format(_site_name)
						else:
							string = '普通权限用户 {} 登录成功!欢迎来到{}!<br><a href="/blogs">点击进入首页</a>'.format(user.username, _site_name)
						res = make_response(render_template_string(string))

					except Exception:
						string = 'try again, kid!<br><a href="/blogs">点击进入首页</a>'
						res = make_response(render_template_string(string))
					res.set_cookie(COOKIE_KEY, username_to_cookie(username))
					return res
		flash('登录失败')
		return redirect(url_for('signin'))

@app.route('/blogs', methods=['GET', 'POST'])
@login_required
def blogs(username):
	if request.method == 'GET':
		pass
	else:
		content = request.form.get('content', '')
		uid = session.query(User).filter(User.username == username).one().uid
		session.add(Blog(uid=uid, content=content))
	return render_template(
		'blogs.html',
		datum=session.query(Blog, User).filter(Blog.uid == User.uid).all(),
		username=username,
		sitename='{}'.format(_site_name)
                )

@app.route('/now_site_name',methods = ['GET'])
@login_required
def now_site_name(username):
    global _site_name
    if username == 'admin':
        try:
            string = '{}'.format(_site_name)
            res = make_response(render_template_string(string))
        except Exception:
            string = 'try again, kid!'
            res = make_response(render_template_string(string))
        return res

@app.route('/site_name', methods=['POST'])
@login_required
def site_name(username):
	global _site_name
	if username == 'admin':
		name = request.form.get('name', '')
		if name:
			if 'os' in name or 'system' in name:
				flash('haha don\'t fool me!')
			else:
				_site_name = name
				flash('修改成功！')
	return redirect(url_for('blogs'))

@app.route('/u_c4nt_f1nd_th15_f14g_ch3ck3r', methods=['GET'])
def u_c4nt_f1nd_th15_f14g_ch3ck3r():
	try:
		file = open('/flag','r')
		content = file.read()
		file.close()
		sha256 = hashlib.sha256()
		sha256.update(content.encode('utf-8').strip())
		res = sha256.hexdigest()
		if 'flag' in request.args:
			if res == request.args['flag']:
				return make_response('success')
			else:
				return make_response('error')
		else:
			return make_response('error')
	except FileNotFoundError:
		return make_response('error')
	except PersmissionError:
		return make_response('error')


if __name__ == '__main__':
	session.add(User(username=u"杨超越全球粉丝后援会", password = hash_password("jwga1jyq9apYqCGgszYqD8kDg7q8")))
	session.add(User(username=u"cxk鸡你太美", password = hash_password("Nw2Gn34fz03acZYI3UfKAwam815X")))
	session.add(User(username=u"海底小捞越", password = hash_password("UT4Bw48BXxpghzgzulqpaIt7UzL8")))
	session.add(User(username=u"保护我方小越越", password = hash_password("p9biAN9uOElHDttSrsDtxcNSZi5F")))
	session.add(User(username=u"守护越越前排的鹿小怡", password = hash_password("GTrGWTIUWZclKBQ8GnXn5TCdLuWF")))
	session.add(User(username=u"超超越越666", password = hash_password("uMSZzTgZyZCeIii7uAOySFsyELKN")))
	session.add(User(username=u"一只小超越", password = hash_password("nD0pOjaNsOCngh9u5zCniiHOStbY")))
	session.add(User(username='admin', password=hash_password('j1nJa2_i5_g0oD_dEve10pEr5_4re_64D')))
	session.add(Blog(uid=1, content="大家好，我是顶天立地杨超越。"))
	session.add(Blog(uid=2, content="我喜欢唱、跳、Rap还有篮球和开源！"))
	session.add(Blog(uid=3, content="最爱杨超越，初来乍到，请多关照​"))
	session.add(Blog(uid=4, content="超越妹妹笑颜，超级治愈，是我心里第一初恋脸啊​"))
	session.add(Blog(uid=5, content="@cxk鸡你太美​，cxk是谁，咱也不知道，咱也不敢问！"))
	session.add(Blog(uid=6, content="超越妹妹 520了 我爱你！"))
	session.add(Blog(uid=7, content="超越宝贝多笑哦 想让你开心"))
	app.run(host='0.0.0.0', port=5000,debug=True)
