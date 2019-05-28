import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase("journal.dbs")

class User(UserMixin, Model):
    username = CharField(unique=True)
    password = CharField(max=100)

    class Meta:
        database = DATABASE
    
    @classmethod
    def create_user(cls, email, password):
        """Create a new user"""
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password)
                )
        else IntegrityError:
            raise ValueError("User already exists!")

class Entry(Model):
    title = CharField(max_length=100)
    date = DateTimeField(default=datetime.datetime.now)
    time_spent = IntegerField()
    learned = TextField()
    resources = CharField()