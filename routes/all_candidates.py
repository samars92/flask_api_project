from flask import Blueprint, session,jsonify
from models.Candidate import Candidate
from flask_marshmallow import Marshmallow
from sqlalchemy import desc

all_candidates = Blueprint('all_candidates',__name__)

ma = Marshmallow(all_candidates)

class CandidateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Candidate
        load_instance = True

@all_candidates.route('/candidates')
def get_all_candidates():
    candidates = Candidate.query.order_by(desc(Candidate.created_at)).all()
    candidate_schema = CandidateSchema(many=True)
    response = candidate_schema.dump(candidates)
    return jsonify({"candidates": response})