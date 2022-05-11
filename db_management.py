from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configurations

engine = create_engine(configurations.connection_string)
conn = engine.connect()
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False, unique=True)


def create_tables():
    Base.metadata.create_all(engine)


def create_connection():
    engine = create_engine('sqlite:///data_base.db')
    conn = engine.connect()
    Session = sessionmaker(bind=engine)
    Base = declarative_base()


def check_user_exists(str_username, str_pass):
    Session = sessionmaker(bind=engine)
    session = Session()

    user_count = session.query(User).filter\
        (User.Username == str_username and User.Password == str_pass).count()
    return user_count > 0


def is_username_taken(username):
    Session = sessionmaker(bind=engine)
    session = Session()

    user_count = session.query(User).filter \
        (User.Username == username).count()
    if user_count > 0:
        return False
    return True


def create_new_user(username_text, pass_text):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(Username=username_text, Password=pass_text)
    try:
        session.add(new_user)
        session.commit()
        return True
    except: # why except? check all ppssible reasons.
        return False

