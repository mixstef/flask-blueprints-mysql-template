# Flask with Blueprints + MySQL basic template
This is a simple template for creating flask apps with mysql support.

**NOTE:** MySQL must be already installed in your system! Moreover, the following example assumes that sample content exists in mysql db. Check subfolder `data` for details.

**NOTE2:** This template uses `mysqlclient` python module. This depends on some C libraries that must be installed on your system (see: [https://github.com/PyMySQL/mysqlclient-python](https://github.com/PyMySQL/mysqlclient-python)).

For example, on Ubuntu, install the following:

	sudo apt-get install python-dev python3-dev libmysqlclient-dev


## Initialization
Follow these steps to initialize your working environment.

### Fork and clone repository

a) Fork this repository. This will allow you to work on your own repository. **No pull request is needed**.

b) Log into the development machine. Clone your forked repository there:

	mkdir my-app
	cd my-app
	git clone <your-github-path> .

**NOTE:** `<your-github-path>` must be replaced by the path to your own repository!


### Prepare the virtual environment (venv)

 
At the project's root folder, enter the following commands at terminal:

	virtualenv venv -p python3
	. venv/bin/activate
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt 

### Create folder with env vars
In project's top folder create a new subfolder `secrets`. This must not be put under version control! In this new folder create a file `env_vars` with the following content:

	export MY_APP_PORT=<your-assigned-port>
	export MY_APP_PREFIX=/<your-assigned-prefix>

	export MY_APP_DB_NAME=<test-db-name>
	export MY_APP_DBUSER_NAME=<test-db-user-name> 
	export MY_APP_DBUSER_PASSWORD=<test-db-user-password>

	export FLASK_APP=myapp

**NOTE:** `<your-assigned-port>` and `<your-assigned-prefix>` must be replaced by the actual data provided to you!.

**NOTE:** In this template, a test user connects to a test db and fetches sample data. `<test-db-name>`, `<test-db-user-name>` and `<test-db-user-password>` should be set according to your experimental db setup.

## Running the test server
Before running the server you should activate venv (if not already active):

	. venv/bin/activate

Enter the following commands to start the testing flask server (with reloading):

	. secrets/env_vars
	flask run --reload --host=0.0.0.0 --port $MY_APP_PORT

## Test access

Cmd:

	curl 'localhost:<your-assigned-port>/<your-assigned-prefix>/' -v

