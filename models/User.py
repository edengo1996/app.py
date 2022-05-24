from sqlalchemy import Column, Integer, String
import configurations


class User(configurations.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False, unique=True)
