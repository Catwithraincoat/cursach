from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('users.id'))
    to_user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(Text)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    password_hash = Column(String(100))
    login = Column(String(32))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey('race.id'))
    name = Column(String(32))
    age = Column(Integer)
    state = Column(String(10))
    relationship = Column(String(10))
    date_of_death = Column(String(50))

class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    appearance = Column(Text)
    personality = Column(Text)

class Enemy(Base):
    __tablename__ = 'enemy'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    reason = Column(String(50))

class Companion(Base):
    __tablename__ = 'companion'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    first_journey_id = Column(Integer, ForeignKey('journey.id'))

class Journey(Base):
    __tablename__ = 'journey'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    time_id = Column(Integer, ForeignKey('time.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    description = Column(Text)

class Race(Base):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    state = Column(String(50))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey('race.id'))
    coordinates = Column(Integer)

class Time(Base):
    __tablename__ = 'time'
    id = Column(Integer, primary_key=True)
    timerfbuinverse = Column(String(50))
    timerfbplanet = Column(String(50))

# Character_In_Journey = Table('character_in_journey', Base.metadata,
#     Column('character_id', Integer, ForeignKey('character.id'), primary_key=True),
#     Column('journey_id', Integer, ForeignKey('journey.id'), primary_key=True)
# )
class Character_In_Journey(Base):
    __tablename__ = 'character_in_journey'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    journey_id = Column(Integer, ForeignKey('journey.id'), primary_key=True)
