from peewee import *
db = SqliteDatabase('pattern.db', field_types={'points': 'text'})