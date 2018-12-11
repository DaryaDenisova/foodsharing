import sqlite3

# connect ar database - in local file app.db
conn = sqlite3.connect('app.db')

#
#CREATE A CURSOR - a
 ##
c = conn.cursor()

c.execute('''
CREATE TABLE offer(
    offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    description TEXT,
    location TEXT,
    station_id INTEGER, 
    giver_id INTEGER,  
    date TEXT,
    time TEXT,
    FOREIGN KEY (giver_id) REFERENCES users(user_id),
    FOREIGN KEY (station_id) REFERENCES metro_station (station_id)
)
''')


c.execute('''
CREATE TABLE users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    rating TEXT,
    offers_given INTEGER,
    offers_takes INTEGER,
    FOREIGN KEY (offers_given) REFERENCES offer(offer_id),
    FOREIGN KEY (offers_takes) REFERENCES offer(offer_id)
)
''')

c.execute('''
CREATE TABLE deal_agreement(
    offer_id INTEGER,
    giver_id INTEGER,
    taker_id INTEGER,
    giver_rating INTEGER,
    taker_rating INTEGER,
    time TEXT,
    FOREIGN KEY (offer_id) REFERENCES offer(offer_id),   
    FOREIGN KEY (giver_id) REFERENCES users(user_id),
    FOREIGN KEY (taker_id) REFERENCES users(user_id),
    FOREIGN KEY (giver_rating) REFERENCES users(rating),
    FOREIGN KEY (taker_rating) REFERENCES users(rating)
)
''')


c.execute('''
CREATE TABLE metro_station(
    station_id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_name TEXT
)
''')

conn.commit()
# adding some data

c.execute ('''
    INSERT INTO offer (name, category, description, location, giver_id,  date, time)
    VALUES ('chocolate', 'sweet', 'ostalos mnogo shokolada s novogo goda', 'nevsky prospekt', '10', '15.01.2018', '19:00'),
    ('tomatoes amd cucumbers', 'vegetable', 'svoi ovoschi s gryadki', 'kupchino', '5', '08.08.2018', '12:00'),
    ('apples', 'fruit', 'narvali u sosedeq, ochen vkusnye', 'prospekt veteranov', '12', '17.09.2018', '10:00'),
    ('bulochki', 'bread', 'darim schastiye i svejie bulochki v vash dom', 'pekarnya volcheka', '2', '12.12.2018', '23:00'),
    ('porridge', 'croup', 'navarila kashi na ves rayon', 'sennaya ploshad', '1', '21.12.2018', '11:00'),
    ('zubatka', 'fish', 'zapaha vrode net', 'zvezdnaya', '11', '11.12.2018', '20:00'),
    ('sea kale', 'sea food', 'pokazalas ne vkusnoy', 'rybatskoe', '2', '10.01.2018', '21:00'),
    ('wine', 'alcohol', 'otdam 2 butylki krasnogo', 'devyatkino', '6', '02.02.2018', '18:00'),
    ('provencal herbs', 'spice', 'klevye travy, no ne na moy vkus', 'petrogradskaya', '22', '16.10.2018', '14:00'),
    ('pumpkin seeds', 'nuts and seeds', 'ya takoye ne em', 'mejdunarodnaya', '16', '14.11.2018', '19:00'),
    ('semena', 'nuts and seeds', 'godnota dlya popugov', 'lomonosovskaya', '17', '18.11.2018', '14:00'), 
    ('potato soup', 'ready mix', 'ot babushki', 'avtovo', '11','02.09.2018', '14:30'), 
    ('pertushka', 'green', 'iz svoego ogoroda', 'zvenigorodskaya', '10', '11.11.2018', '15:30'), 
    ('izabella', 'wine', 'podarili na prazdnik', 'dostoevskaya', '7', '7.08.2018', '18:30'), 
    ('granatovoye', 'wine', 'ne lublu vino', 'parnas', '6', '14.09.2018', '18:20'), 
    ('water melon', 'fruits and vegetables', 'ochen mnogo na dache', 'devyatkino', '3', '19.08.2018', '10:20'), 
    ('cucumbers', 'fruits and vegetables', 's dachi vezy', 'devyatkino', '9', '19.08.2018', '11:40'), 
    ('choco bins', 'nuts and seeds', 'podarili a u menya allergiya', 'devyatkino', '2', '20.10.2018', '12:00'), 
    ('moloko', 'dairy', 'iz nastoyashi korovy', 'sennaya ploschad', '12', '20.10.2018', '11:00'), 
    ('bulka hleba', 'bread', 'pud hleba razdaet podarki', 'nevsky prospekt', '8', '20.10.2018', '13:30'), 
    ('choco bins', 'nuts and seeds', 'priverly iz kitaya', 'sadovaya', '11', '20.10.2018', '14:00');

''')
#MANY TO MANY
c.execute('''
    CREATE TABLE users_offer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        offer_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(offer_id) REFERENCES offer(offer_id)
        )
''')

conn.commit()
