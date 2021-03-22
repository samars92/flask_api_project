from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db import db
from flask import json, request
import os
from routes.register import register
from routes.download_resume import download_resume
from routes.all_candidates import all_candidates

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://mariadb:maria@localhost/hr_system'
db.init_app(app)
migrate=Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

app.register_blueprint(register)
app.register_blueprint(download_resume)
app.register_blueprint(all_candidates)
 
if __name__ == "__main__":
     app.run(debug=True)