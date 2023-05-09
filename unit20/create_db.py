import datetime

from sqlalchemy import create_engine, Column, Integer, Text, Date, Float, Boolean, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    @classmethod
    def get_all_books(cls):
        return session.query(Books).all()

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

class Authors(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_students_with_scholarship(cls):
        return session.query(Students).filter(Students.scholarship)

    @classmethod
    def get_students_with_higher_score(cls, score):
        return session.query(Students).filter(Students.average_score > score)

class ReceivingBooks(Base):
    __tablename__ = "receiving_books"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @classmethod
    def get_debtors(cls):
        return session.query(ReceivingBooks).all()

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is None:
            return (datetime.datetime.now() - self.date_of_issue).days
        else:
            return (self.date_of_return - self.date_of_issue).days

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

Base.metadata.create_all(bind=engine, checkfirst=True)