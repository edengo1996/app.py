from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configurations
from signup_utils import SignupResults
from models.User import User


engine = create_engine(configurations.connection_string, connect_args={'check_same_thread': False})
session_made = sessionmaker(bind=engine)


def create_connection():
    return engine.connect()


def create_tables():
    configurations.Base.metadata.create_all(engine)


def check_login_parameters(username: str, password: str) -> bool:
    session = session_made()

    user_count = session.query(User).filter(
        User.Username == username and User.Password == password).count()
    return user_count == 1


def is_username_not_taken(username: str) -> bool:
    session = session_made()

    user_count = session.query(User).filter(
        User.Username == username).count()
    return user_count == 0


def create_new_user(username: str, password: str) -> int:
    session = session_made()

    if session.query(User).filter(User.Username == username).count() == 1:
        return SignupResults.USERNAME_TAKEN

    new_user = User(Username=username, Password=password)
    try:
        session.add(new_user)
        session.commit()
        return SignupResults.SUCCESSFUL_SIGNUP
    except:
        return SignupResults.DB_COMM_ERROR
