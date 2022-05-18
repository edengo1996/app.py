from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configurations
from signup_utils import SignupResults
from models.User import User

engine = create_engine(configurations.connection_string, connect_args={'check_same_thread': False})
Base = declarative_base()


def create_connection():
    return engine.connect()


def create_tables():
    Base.metadata.create_all(engine)


def check_login_parameters(username: str, password: str) -> bool:
    session_made = sessionmaker(bind=engine)
    session = session_made()

    user_count = session.query(User).filter(
        User.Username == username and User.Password == password).count()
    return user_count > 0


def is_username_not_taken(username: str) -> bool:
    session_made = sessionmaker(bind=engine)
    session = session_made()

    user_count = session.query(User).filter(
        User.Username == username).count()
    return user_count == 0


def create_new_user(username_text: str, pass_text: str) -> int:
    session_made = sessionmaker(bind=engine)
    session = session_made()

    new_user = User(Username=username_text, Password=pass_text)
    try:
        session.add(new_user)
        session.commit()
        return SignupResults.SUCCESSFUL_SIGNUP
    except:
        return SignupResults.DB_COMM_ERROR
