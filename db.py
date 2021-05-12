import sqlite3

from config import db_path

def create_table():
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artist (name TEXT UNIQUE, age NUMBER) ')
        conn.close()
    except Exception as e:
        print('Error creating table', e)


def add_artist(artist):
    """ return True if artist added, False if error adding. TODO distingush sucess, duplicate, other error."""
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute('INSERT INTO artist VALUES (?, ?)', (artist.name, artist.age))
        conn.close()
        return True 
    except Exception as e:
        # todo check if constraint violation for duplicate name 
        print('duplicate artist', e)
        return False


# def create_table():
#     # creating a anew table with 3 columns
#     try:
#         with sqlite3.connect(db) as conn:  
#             conn.execute('create table if not exists records (name text UNIQUE, age number)')
#         conn.close()
#     except Exception as e:
#         print('Error creating a table')
