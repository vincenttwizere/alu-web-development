#!/usr/bin/env python3
"""
Module that defines the User class for SQLAlchemy ORM.

This module contains the User class, which represents a user
in the database with fields for id, email, hashed_password,
session_id, and reset_token. It is used to manage user-related
data in the system.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """User class represents a user record in the database."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
