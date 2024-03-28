from models import Race, Character, Doctor, Planet, Time, Journey, Enemy, Companion, Users, Message, Character_In_Journey
from db import Session
import csv
# Import necessary models from models module

session = Session()  # Create a session object

tables = ['Race', 'Character', 'Doctor', 'Planet', 'Time', 'Journey', 'Enemy', 'Companion', 'Users', 'Message', 'Character_In_Journey']


for table in tables:

    with open(f"../db/csvs/{table}.csv", 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Iterate over the rows and create instances of the corresponding model
    for row in data:
        if 'id' in row:
            del row['id']
 
        for key in row:
            if row[key] == '':
                row[key] = None
        print(row)
        if table == 'Race':
            instance = Race(**row)
        elif table == 'Character':
            instance = Character(**row)
        elif table == 'Doctor':
            instance = Doctor(**row)
        elif table == 'Planet':
            instance = Planet(**row)
        elif table == 'Time':
            instance = Time(**row)
        elif table == 'Journey':
            instance = Journey(**row)
        elif table == 'Enemy':
            instance = Enemy(**row)
        elif table == 'Companion':
            instance = Companion(**row)
        elif table == 'Users':
            instance = Users(**row)
        elif table == 'Message':
            instance = Message(**row)
        elif table == 'Character_In_Journey':
            instance = Character_In_Journey(**row)

        session.add(instance)  # Add the instance to the session
        session.commit()  # Commit the changes to the database

    session.commit()  # Commit the changes to the database

session.close()  # Close the session
