from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    designation = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    is_deleted = db.Column(db.Integer, nullable=False, default='0')

    def __repr__(self):
        return ({self.name}, {self.designation}, {self.address}, {self.phone})