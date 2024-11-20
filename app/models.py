from . import db

class Link(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=True)
    password = db.Column(db.Text, nullable=False)
    data = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f"{self.name}"