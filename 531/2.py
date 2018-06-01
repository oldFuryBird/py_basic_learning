# flask-wtf 扩展
# WTForms
from flask import Flask,render_template
from flask_script import Manager
from flask_wtf import Form
from wtforms.validators import Required
from wtforms.WTForms import StringField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index(name):
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('form.html',form = form ,name=name)
	# return 'hello',name

if __name__ == '__main__':
	manager.run()