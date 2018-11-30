import sqlite3

# connect ar database - in local file app.db
conn = sqlite3.connect('app.db')

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
    giver_id INTEGER,  
    taker_id INTEGER,
    time of the deal TEXT,
    FOREIGN KEY (taker_id) REFERENCES users(user_id), 
    FOREIGN KEY (giver_id) REFERENCES users(user_id)
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

conn.commit()
# adding some data

c.execute ('''
    INSERT INTO offer (offer_id, name, category, description, location, giver_id, taker_id, time of the deal)
    VALUES ('1', 'chocolate', 'sweet', 'ostalos mnogo shokolada s novogo goda', 'nevsky prospekt', '10', '4', '15/01, 19:00');

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