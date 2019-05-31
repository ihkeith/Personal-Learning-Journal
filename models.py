from peewee import *

DATABASE = SqliteDatabase('learning_journal.db')

class Entry(Model):
    title = CharField(max_length=255)
    date = DateField()
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date',)
    
    @classmethod
    def create_entry(cls, title, date, time_spent, learned, resources):
        with DATABASE.transaction():
            cls.create(
                title=title,
                date=date,
                time_spent=time_spent,
                learned=learned,
                resources=resources
            )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()