# 请求钩子
# before_first_request 注册一个函数，在处理第一个请求之前运行
# before_request 注册一个函数，每次请求之前运行
# after_request 如果没有异常抛出，每次请求之后运行
# teardown_request 有异常抛出也在每次请求之后运行

# g 

# 相应 Flask 默认为200，表明请求已经被成功处理
# make_response
# redirect 跳转
# abort 特殊相应 abort(404)

# flask 扩展 flask.ext 

from flask import Flask 
from flask import make_response
app = Flask(__name__)

# @app.route('/')
# def index():
# 	return 'hello';

@app.route('/bad')
def bad():
	return '<h1>bad request</h1>', 400

@app.before_first_request
def action():
	print('123')

# make_response()
@app.route('/')
def index():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response


if __name__ == '__main__':
	app.run()