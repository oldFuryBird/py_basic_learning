from flask import Flask
from flask import request # 临时上下文让某些对象变成全局访问 封装客户端发出的http请求全部内容
from flask import current_app # 当前激活程序的实例 
from flask import g # 处理请求时用于临时存储的对象，每次请求都会重置
from flask import session # 用户回话
# 每个线程看到的request对象必然不同
# __name__ flask 根据这个参数决定程序的根目录，以便稍后能找到相对于程序根目录的资源文件位置

# 多线程web服务器会创建一个线程池，再从线程池中选择一个线程用于处理接收到的请求

app = Flask(__name__)
# 在代码中嵌入响应字符串会导致代码难以维护
@app.route('/')
def index():
	'''index 成为视图函数 view function '''
	user_agent = request.headers.get('User-Agent')
	print(current_app.name)
	print(dir(current_app))
	return '<h1>Your browser is %s</h1> ' % user_agent

@app.route('/user/<name>')
def user(name):
	'''flask 支持在路由中使用int,float,path类型'''
	return '<h1>Hello ,%s!</h1>' % name



# start the web app
if __name__ == '__main__':
	'''__name__ == '__main__' 是python的惯用方法，确保执行这个脚本时才会启动开发web服务器，如果这个脚本由其他脚本引入，程序的父脚本不会执行app.run'''
	app.run(debug=True)