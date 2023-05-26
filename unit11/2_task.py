import requests
import sqlite3
from sqlalchemy import create_engine, Column, Integer, Text, Date
from sqlalchemy.orm import sessionmaker, declarative_base

PAGE_COUNT = 1
QUANTITY = 20
PERSONS = []

engine = create_engine("sqlite:///starwars.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Persons(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    birth_year = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)

def record_data():
    session.bulk_insert_mappings(Persons, PERSONS)
    session.commit()

def star_wars_api():
    global PAGE_COUNT
    global QUANTITY
    global PERSONS
    count = QUANTITY - (PAGE_COUNT - 1) * 10
    people = requests.get(f'https://swapi.dev/api/people/?page={PAGE_COUNT}').json()
    if count >= 0:
        try:
            for i in range(count):
                person = {"name": people['results'][i]['name'],
                          "birth_year": people['results'][i]['birth_year'],
                          "gender": people['results'][i]['gender']}
                PERSONS.append(person)
        except IndexError:
            if QUANTITY >= people['count']:
                print('Incorrect request')
                exit()
            else:
                PAGE_COUNT += 1
                star_wars_api()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine, checkfirst=True)
    star_wars_api()
    record_data()