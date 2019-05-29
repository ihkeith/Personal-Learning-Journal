import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase("learning_journal.db")

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)

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
        except IntegrityError:
            raise ValueError("User already exists!")

class Entry(Model):
    title = CharField(max_length=100)
    date = DateTimeField(default=datetime.datetime.now)
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()
    user = ForeignKeyField(
        User,
        related_name='entries'
    )

    class Meta:
        database = DATABASE


class Tag(Model):
    tag = CharField(max_length=100)
    post = ForeignKeyField(
        Entry,
        related_name='tags'
    )

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Entry, Tag], safe = True)
    DATABASE.close()