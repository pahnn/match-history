from ..core import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer(), primary_key=True)
    profile_icon_id = db.Column(db.String())
    name = db.Column(db.String())
    puuid = db.Column(db.String())
    summoner_level = db.Column(db.Integer())
    summoner_id = db.Column(db.String())
    account_id = db.Column(db.String())
    revision_date = db.Column(db.Integer())
    last_fetched_date = db.Column(db.Integer())
            

