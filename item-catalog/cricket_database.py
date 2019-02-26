import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
            }


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable formate"""
        return {
            'name': self.name,
            'id': self.id
            }


class Player(Base):
    __tablename__ = 'player'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    about = Column(String(250))
    jersey_number = Column(String(10))
    runs = Column(String(20))
    half_century = Column(Integer)
    century = Column(Integer)
    place = Column(String(100))
    player_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable formate"""
        return{
            'name': self.name,
            'about': self.about,
            'id': self.id,
            'jersey_number': self.jersey_number,
            'runs': self.runs,
            'half_century': self.half_century,
            'century': self.century,
            'place': self.place,
            'player_id': self.player_id
            }

engine = create_engine('sqlite:///cricketplayer.db')

Base.metadata.create_all(engine)
