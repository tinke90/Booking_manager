import sqlite3
import threading
import time
from datetime import datetime

class Settings:
    m_database = 'C:\\Users\\<username>\\Documents\\TimeReservationApp\\Database\\database.db'
    m_settings = 'SELECT * FROM Settings'
    m_profile = 'SELECT * FROM Profile'
    m_reservation = 'SELECT * FROM Reservation'

class myThread(threading.Thread):


    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def test():
        print('test')


    def run(self):
        m_counter = 0
        test()
        # LOOP TILL THE PROGRAM QUIT...
        while True:
            
            conn = sqlite3.connect(Settings.m_database)

            cur = conn.cursor()

            cur = conn.execute(Settings.m_reservation)

            result = cur.fetchall()

            _row = 0

            # IF RESULT LIST IS GREATER...IN OTHER WORDS
            # IF RESERVATION TABLE HAS GAIN NEW DATA, PRINT THEM OUT...
            if len(result) > m_counter:
            
                # SHOW ONLY THE LATEST ADDED RESERVATION...
                for item in result:
                    if _row + 1 == len(result):
                        DisplayReservations(item)
                        m_counter = len(result)

                        print()                 # Print extra line...
                        
                    _row = _row + 1
                    
            time.sleep(1.0)


# PRINT PROFILES...FETCH DATA FROM database.db TABLE Profile
def DisplayProfile(str):
    print('______PROFILE ',str[0],'_____')
    print('ID:        ', str[0])
    print('USERNAME:  ', str[1])
    print('PASSWORD:  ', str[2])
    print('EMAI:      ', str[3])
    print('PHONE:     ', str[4])
    print('ACTIVE:    ', str[5])
    print('FIRSTNANE: ', str[6])
    print('LASTNAME:  ', str[7])
    print('BIRTHDATE: ', str[8])

    print()                 # Print extra line...

# PRINT SETTINGS...FETCH DATA FROM database.db TABLE Settings
def DisplaySettings(str):
    print('_____SETTINGS ',str[0],'_____')
    print('ID:      ',str[0])
    print('FUNCTION:',str[1])
    print('USE:     ',str[2])

    print()                 # Print extra line...
    
# PRINT SCHEDULE...FETCH DATA FROM database.db TABLE Reservation
def DisplayReservations(str):
    print('____RESERVATION ',str[0],'___')
    print('ID:            ', str[0])
    print('FIRSTNAME:     ', str[1])
    print('LASTNAME:      ', str[2])
    print('RESERVATION:   ', str[3])
    print('RESERVED TIME: ', str[4])
    print('RESERVED DATE: ', str[5])
    print('DATE:          ', str[6])

    print()                 # Print extra line...

# RECEIVE COMMANDS...
def Command(INPUT):
    conn = sqlite3.connect(Settings.m_database)

    cur = conn.cursor()

    if INPUT == 'profile':
        cur = conn.execute(Settings.m_profile)
        result = cur.fetchall()

        for row in result:
            DisplayProfile(row)

    elif INPUT == 'settings':
        cur = conn.execute(Settings.m_settings)
        result = cur.fetchall()

        for row in result:
            DisplaySettings(row)

    elif INPUT == 'reservation':
        cur = conn.execute(Settings.m_reservation)
        result = cur.fetchall()

        for row in result:
            DisplayReservations(row)

    else:
        print('=Unknown command=')


def Main():

    print('Booking manager')

    thread = myThread(1, 'Thread-1', 1)
    thread.start()

    loop = True

    while loop:
        
        print()                 # Print extra line...

        INPUT = input('> ')

        print()                 # Print extra line...

        try:
            if INPUT == 'exit':
                loop = False
                thread._stop()

            Command(INPUT)
        except:
            print("shutted down...")


Main()

