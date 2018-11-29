from sqlalchemy import create_engine, Column, String, Integer, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite://twitter.db')
Base = declarative_base()

# # td = datetime.datetime(2018, 2, 22, 23, 34)
# # donly = datetime.date(2018, 2, 19)


class User(Base):

    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True)
    handle = Column(String, nullable=False)
    join_date = Column(Date)

    tweets = relationship('Tweet', back_populates='user')


class Tweet(Base):

    __tablename__ = 'tweet'

    tid = Column(Integer, primary_key=True)
    tweet_timestamp = Column(DateTime)
    user = relationship('User', back_populates='tweets')
    author = Column(Integer, ForeignKey('user.id'))


Base.metadata.create_all(engine)
