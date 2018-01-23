from flask import Blueprint,render_template

from ..app import mysql


hello = Blueprint('hello',__name__)


@hello.route('/')
def index_page():

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM employee')
	results = c.fetchall()
	return render_template('index.html',results=results)

