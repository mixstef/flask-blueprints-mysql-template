import os

from flask import Flask
import MySQLdb


class MySQL:

	def __init__(self,app=None):
		self.db = None
		if app is not None:
			self.init_app(app)
			
	def init_app(self,app):
		
		if not self.db:
			host = app.config['MYSQL_HOST']
			port = app.config['MYSQL_PORT']
			user = app.config['MYSQL_USER']
			passwd = app.config['MYSQL_PASSWORD']
			db = app.config['MYSQL_DB']
			
			self.db = MySQLdb.connect(host=host,port=port,
						  user=user,passwd=passwd,
						  db=db)
			



def create_app():
	
	app = Flask(__name__)
		
		
	# mysql connection details
	app.config['MYSQL_HOST'] = os.environ.get('MY_APP_DB_HOST','127.0.0.1')
	app.config['MYSQL_PORT'] = os.environ.get('MY_APP_DB_PORT',3306)	
	app.config['MYSQL_USER'] = os.environ['MY_APP_DBUSER_NAME']
	app.config['MYSQL_PASSWORD'] = os.environ['MY_APP_DBUSER_PASSWORD']	
	app.config['MYSQL_DB'] = os.environ['MY_APP_DB_NAME']
						 
	# configure mysql
	mysql.init_app(app)	
	
	# common prefix for all routes in blueprints
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
	# register all blueprints
	from .views import blueprints
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)
		
		
	return app


mysql = MySQL()	
app = create_app()	
	
