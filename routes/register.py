from flask import Blueprint, session,abort
from flask import json, request
from werkzeug.utils import secure_filename
from models.Candidate import Candidate, Department
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import AWS_BUCKET_NAME,s3

register = Blueprint('register',__name__)
@register.route('/register', methods=["POST"])
def registerCandidate():
    data = request.form
    if data.get('name') and data.get('department_id') and data.get('department_id') in Department.__members__:
        content_type = request.mimetype
        file = request.files['file']
        filename = secure_filename(file.filename)  # This is convenient to validate your filename, otherwise just use file.filename
        if file:
            try:
                print(filename)
                s3.put_object(Body=file,
                        Bucket=AWS_BUCKET_NAME,
                        Key=filename,
                        ContentType=content_type)

            except Exception as e:
                print("Something Happened: ", e)
                return e
        
        name = data.get('name')
        date_of_birth = datetime.strptime(data.get('date_of_birth'),'%Y-%m-%d')
        years_of_experience = data.get('years_of_experience')
        department_id = data.get('department_id')
        resume_filename = filename

        candidate = Candidate(
            name=name,
            date_of_birth=date_of_birth,
            years_of_experience=years_of_experience,
            department_id=department_id,
            resume_filename=resume_filename
        )

        candidate.save()

        return json.dumps({'status': 200, 'message': 'User added successfully'}), 200

    return json.dumps({'status': 'fail', 'message': 'Name and Department are required'}), 400