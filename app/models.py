from . import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    published_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Book {self.title}>"

