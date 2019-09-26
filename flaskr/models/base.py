from peewee import *
from playhouse.db_url import connect
from flaskr import app
database = MySQLDatabase('xisitan', user='root', passwd='password',
                          host='localhost')

def connect_db():
    if database.is_closed():
        database.connect()

def close_db(exc):
    if not database.is_closed():
        database.close()

app.before_request(connect_db)
app.teardown_request(close_db)

class BaseModel(Model):
    class Meta:
        database = database # This model uses the "people.db" database.

class todoModel(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    event = CharField()
    begin_time = CharField()
    if_done = BooleanField()
    
def create_tables():
    with database:
        database.create_tables([todoModel])

create_tables()
# grandma = Person.create(name='Grandma')
# grandma.name = 'Grandma L.'
# grandma.save()