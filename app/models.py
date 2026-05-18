from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    sonuc = db.Column(db.String(100))
    detay = db.Column(db.Text)
    skor = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)