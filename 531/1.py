from flask import Flask ,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'

# 链接 
# url_for 以视图函数名 app.add_url_route()定义路由时使用的端点名 返回对应的URL
# _external True 显示绝对路径
# 程序内不同的路由链接，相对地址就足够
# 浏览器之外使用的链接，必须使用绝对地址
# 如在电子邮件中发送的链接
# url_for('static', filename='css/styles.css',_external=True )
# http://localhost:5000/static/css/styles.css

@app.route('/test')
def test1():
	# return url_for('index',_external = True)
	# return url_for('test1',name='test',_external = True)
	 return url_for('static',filename='css/styles.css',_external = True)

# Flask-Monment moment.js  format() fromNow() fromTime() calendar() valueOf() unix() 方法

if __name__ == '__main__':
	app.run()