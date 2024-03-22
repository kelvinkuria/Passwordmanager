# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    master_password = Column(String)
    salt = Column(String)

    accounts = relationship("Account", back_populates="user")

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    website = Column(String)
    username = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="accounts")
    passwords = relationship("Password", back_populates="account")

class Password(Base):
    __tablename__ = 'passwords'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    encrypted_password = Column(String)

    account = relationship("Account", back_populates="passwords")