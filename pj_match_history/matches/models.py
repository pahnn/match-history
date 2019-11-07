from ..core import db
from sqlalchemy.dialects.postgresql import JSON

class Match(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer(), primary_key=True)
    account_id = db.Column(db.Integer())
    # queue_id = db.Column(db.Integer())
    # season_id = db.Column(db.Integer())
    game_id = db.Column(db.Integer())
    # participant_identities = db.Column(JSON)
    # game_version = db.Column(db.String())
    # platform_id = db.Column(db.String())
    # game_mode = db.Column(db.String())
    # map_id = db.Column(db.Integer())
    # game_type = db.Column(db.String())
    # teams = db.Column(JSON)
    # participants = db.Column(JSON)
    # game_duration = db.Column(db.Integer())
    # game_creation = db.Column(db.Integer())
            