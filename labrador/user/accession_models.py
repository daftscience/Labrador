# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from labrador.database import Column, Model, SurrogatePK, db, reference_col, relationship
from labrador.extensions import bcrypt


class Accession(SurrogatePK, Model):
    """An Accession number to file"""
    __tablename__ = 'accession'

    number = Column(db.String(80), unique=True, nullable=False)
    location = db.relationship('Location', backref='location', lazy='dynamic')
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, number=kwargs.pop('number'), **kwargs)

    def add_series(self, col, row):
            self.location.append(col, row)
            db.session.add(self)
            db.session.commit()


class Location(SurrogatePK, Model):
    __tablename__ = 'location'
    column = Column(db.String(10))
    row = Column(db.String(10))
    created_at = Column(
        db.DateTime,
        nullable=False,
        default=dt.datetime.utcnow)
