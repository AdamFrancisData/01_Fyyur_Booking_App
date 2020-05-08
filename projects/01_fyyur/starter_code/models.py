"""
Venue, Artist, Show Classes
"""
from app import db


class Shared(db.Model):
    """
    Base class with shared attributes to inherit from
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String(120))
    city = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    state = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.name)

class Venue(Shared):
    """
    Venue Model derived from 'Shared' class
    """
    __tablename__ = 'venue'

    address = db.Column(db.String(120))
    shows = db.relationship('Show', backref='venue', lazy=True)


class Artist(Shared):
    """
    Artist Model derived from 'Shared' class
    """
    __tablename__ = 'artist'

    shows = db.relationship('Show', backref='artist', lazy=True)


class Show(db.Model):
    """
    Show Model
    """
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)
