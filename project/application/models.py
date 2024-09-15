from extensions import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    books = db.relationship('Book', backref='owner', lazy="select")

    def __init__(self, username, password, email, is_admin=False):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.is_admin = is_admin

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self) 
        db.session.commit()




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.LargeBinary) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, title, image=None, user_id=None):
        self.title = title
        self.image = image
        self.user_id = user_id

    def add_book(self):
        db.session.add(self) 
        db.session.commit()

    def delete_book(self):
        db.session.delete(self)
        db.session.commit()