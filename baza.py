##baza danuch na bazie SQLite i system ORM Peewee

from peewee import *
from datetime import datetime

baza = SqliteDatabase('adresy.db')

#klada bazowa
class BazaModel(Model):
    class Meta:
        database = baza
        
class Osoba(BazaModel):
    login = CharField(null=False, unique=True)
    haslo = CharField()
    
    class Meta:
        order_by = ('login',)
        
class Zadanie(BazaModel):
    tresc = TextField(null=False)
    datad = DatabaseField('default=datatime.now')
    wykonane = BooleanField(default=False)
    osoba = ForeignKeyField(Osoba, related_name='zadania')
    
    class Meta:
        order_by = ('datad',)
        
def polacz():
    baza.connect() #nawiązanie połączenia z baza.py
    baza.create_tables([Osoba, Zadanie], True) #tworzy tabele widoczna dla uzytkownia
    ladujDane() #wstawiamy dane
    return True

def loguj(login, haslo):
    try:
        osoba, created = Osoba.get_or_create(login=login, haslo=haslo)
        return osoba
    except IntegrityError:
        return None

def ladujDane():
    """ Przygotowanie początkowych danych testowych """
    if Osoba.select().count() > 0:
        return
    osoby = ('adam', 'ewa')
    zadania = ('Pierwsze zadanie', 'Drugie zadanie', 'Trzecie zadanie')
    for login in osoby:
        o = Osoba(login=login, haslo='123')
        o.save()
        for tresc in zadania:
            z = Zadanie(tresc=tresc, osoba=o)
            z.save()
    baza.commit()
    baza.close()
    
    
        
    