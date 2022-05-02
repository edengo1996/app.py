from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///data_base.db')
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False, unique=True)


def create_connection():
    Base.metadata.create_all(engine)


def check_if_user_exists(str_username, str_pass):
    Session = sessionmaker(bind=engine)
    session = Session()

    user_count = session.query(User).filter\
        (User.Username == str_username and User.Password == str_pass).count()
    if user_count == 0:
        return False
    return True


def check_valid_username(str_input):
    Session = sessionmaker(bind=engine)
    session = Session()

    user_count = session.query(User).filter \
        (User.Username == str_input).count()
    if user_count > 0:
        return False
    return True


def create_new_user(username_text, pass_text):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(Username=username_text, Password=pass_text)
    session.add(new_user)
    session.commit()
