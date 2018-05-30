from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

# 错误页面
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == "__main__":
	app.run()

'''
Jinja2 变量过滤器
safe 渲染值时不转义
capitalize首字符大写
lower 
upper
title 每个单词首字母都转成大写
trim 首尾空格去掉
striptags 渲染之前把值中所有的HTML标签都删除

flask-bootstrap Flask扩展 
'''