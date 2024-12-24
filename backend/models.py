from database import Base
from sqlalchemy import Column, String, Integer

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)

