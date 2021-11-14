import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DSN = 'postgresql://ab:5015@localhost/vkinder'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)


class Client(Base):
    __tablename__ = 'client'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    persons = relationship('Person', secondary='client_person', back_populates='clients', cascade="all,delete",
                           cascade_backrefs=True)


class Person(Base):
    __tablename__ = 'person'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    clients = relationship('Client', secondary='client_person', back_populates='persons', cascade="all,delete",
                           cascade_backrefs=True)
    photos = relationship('Person', backref='person')


client_person = sq.Table(
    'client_person', Base.metadata,
    sq.Column('client_id', sq.Integer, sq.ForeignKey('client.id')),
    sq.Column('person_id', sq.Integer, sq.ForeignKey('person.id')),
    sq.UniqueConstraint('client_id', 'person_id', name='un_cl_per')
)


class Photo(Base):
    __tablename__ = 'photo'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    person_id = sq.Column(sq.Integer, sq.ForeignKey('person.id', ondelete="CASCADE"))


if __name__ == '__main__':
    session = Session()
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print('Создано')
