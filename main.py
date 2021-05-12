""" Example methods from first iteration of program """
from model import Artist
from menu import Menu
import ui
import db


def main():
    setup()
    add_new_artist()



def setup():
    # any tasks the program needs to complete before it can start 
    db.create_table()


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    # menu.add_option('2', 'Search For Book', search_book)
    # menu.add_option('3', 'Show Unread Books', show_unread_books)
    # menu.add_option('4', 'Show Read Books', show_read_books)
    # menu.add_option('5', 'Show All Books', show_all_books)
    # menu.add_option('6', 'Change Book Read Status', change_read)
    # menu.add_option('7', 'Delete Book', delete_book)
    # menu.add_option('Q', 'Quit', quit_program)

    return menu




def add_new_artist():
    name = input('Enter name: ')
    age = int(input('Enter age: '))

    artist = Artist(name, age)
    added = db.add_artist(artist)

    # todo distinguish between added, duplicate, unexpected error 
    if added:
        print('Added artist')
    else:
        print('Duplicate artist')

def show_all_artist_artwork():
    artist_name = .get_artist_name()
    artist_ID =


def add_artwork():
    try:

    except:
        print('\nNo artist found with that name.\n')


def quit_program():


if __name__ == '__main__':
    main()