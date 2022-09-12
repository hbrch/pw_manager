from menu import menu, menu_back
from db_manager import database  
from functools import partial
import sqlite3, hashlib, os, gnupg

gpg = gnupg.GPG(gnupghome='/****/****/.****')
masterpass = os.environ.get('****')
path = '/****/****/****/****/****'
decfile = '/pass.db'
encfile = '/pass.db.encrypted'

#GnuPG Datei 
def encryption():
    print("Beenden...")
    with open(path + encfile, 'rb') as f:
        status = gpg.encrypt_file(f, recipients = ['****@****.****'], output=path + encfile + ".encrypted")
        os.remove("/****/****/****/****/****/****.****")

#DB
database()
with sqlite3.connect('pass.db') as db:
    c = db.cursor()

passw = input("Masterpasswort: ")

if passw == masterpass:
    print("erfolgreich")

else:
    print("ERROR")
    exit()

#Passwort Manager
menu()
eingabe = input(": ")

if eingabe == '1':
    seite_name = input("Seite: ")
    seite_passwort = input("Passwort: ")

    insert_fields = """INSERT INTO vault(website, password) 
    VALUES(?, ?) """
    c.execute(insert_fields, (seite_name, seite_passwort))
    db.commit()
    
    menu_back()
    eingabe_beenden = input(': ')
    
    if eingabe_beenden == '1':
        menu()
    
    elif eingabe_beenden == '2':
        exit()

    elif eingabe_beenden == '3':
        encryption()

elif eingabe == '2':
    if (c.fetchall() != None):
        i = 0
        while True:
            c.execute('SELECT * FROM vault')
            array = c.fetchall()
            print("------------")
            print("Name: ", array[i][1])
            print("Pass: ", array[i][2])
            print("------------")
            
            i = i +1
            c.execute('SELECT * FROM vault')
            if (len(c.fetchall()) <= i):
                break

        menu_back()
        eingabe_beenden = input(': ')
        
        if eingabe_beenden == '1':
            print("Verlassen...")
            exit()
        elif eingabe_beenden == '2':
            encryption()
    
else:
    encryption()
    print("Verlassen...")
    exit()

