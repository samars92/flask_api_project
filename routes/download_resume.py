from flask import Blueprint, session,abort
from flask import json, request
from werkzeug.utils import secure_filename
from models.Candidate import Candidate
from flask_sqlalchemy import SQLAlchemy
from config import AWS_BUCKET_NAME,s3

download_resume = Blueprint('download_resume',__name__)
@download_resume.route('/download-resume/<id>')
def download(id):
    if request.headers.get('X-ADMIN') and request.headers.get('X-ADMIN')  == '1':
        candidate = Candidate.query.get(id)
        filename = candidate.resume_filename
        with open(filename, 'wb') as f:
            s3_response_object = s3.get_object(Bucket=AWS_BUCKET_NAME,
                            Key=filename)
            response = s3_response_object['Body'].read()
        return {'status': 200, 'message': 'File download successfully'}

    return {'status': 400, 'message': 'Access for admins only'}