# flask_api_project

How to run:
* git clone https://github.com/samars92/flask_api_project.git
* cd flask_api_project
* virtualenv -p python3 venv
* source ./venv/bin/activate
* pip install -r requirements.txt

db init and migrate:
* brew install mariadb
* mysql.server start
* sudo mysql -u root
* flask db init
* flask db migrate
* flask db upgrade

for s3 configuration:
* in config.py file add aws s3 bucket_name, access_key and secret_key
