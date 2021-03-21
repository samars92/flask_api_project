import datetime
from flask_sqlalchemy import SQLAlchemy
from db import db
from enum import Enum

## this to be moved in a seperate model if departments in database
class Department(Enum):
    IT = 0
    HR = 1
    Finance = 2

class Candidate(db.Model):
  __tablename__ = 'candidate'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  date_of_birth = db.Column(db.DateTime)
  years_of_experience = db.Column(db.Integer)
  department_id = db.Column(db.Integer)
  resume_filename = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime)

  def get_all():
    return Candidate.query.all()

  # class constructor
  def __init__(self, name, date_of_birth, years_of_experience, department_id, resume_filename):
    self.name = name
    self.date_of_birth = date_of_birth
    self.years_of_experience = years_of_experience
    self.department_id = department_id
    self.resume_filename = resume_filename
    self.created_at = datetime.datetime.utcnow()


  def save(self):
    db.session.add(self)
    db.session.commit()

  
  def __repr(self):
    return json.dumps(self.__dict__)
