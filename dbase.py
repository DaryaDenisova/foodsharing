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
    login TEXT
)
''')

c.execute('''
CREATE TABLE deal_agreement(
    offer_id INTEGER,
    giver_id INTEGER,
    taker_id INTEGER,
    time TEXT,
    FOREIGN KEY (offer_id) REFERENCES offer(offer_id),   
    FOREIGN KEY (giver_id) REFERENCES users(user_id),
    FOREIGN KEY (taker_id) REFERENCES users(user_id)
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
    INSERT INTO offer (name, category, description, location, station_id, giver_id,  date, time)
    VALUES ('chocolate', 'sweet', 'ostalos mnogo shokolada s novogo goda', 'nevsky prospekt', '27', '10', '15.01.2018', '19:00'),
    ('tomatoes amd cucumbers', 'vegetable', 'svoi ovoschi s gryadki', 'kupchino', '36', '5', '08.08.2018', '12:00'),
    ('apples', 'fruit', 'narvali u sosedeq, ochen vkusnye', 'prospekt veteranov', '18', '12', '17.09.2018', '10:00'),
    ('bulochki', 'bread', 'darim schastiye i svejie bulochki v vash dom', 'proletarskaya', '46', '2', '12.12.2018', '23:00'),
    ('porridge', 'croup', 'navarila kashi na ves rayon', 'sennaya ploshad', '28', '1', '21.12.2018', '11:00'),
    ('zubatka', 'fish', 'zapaha vrode net', 'zvezdnaya', '35', '11', '11.12.2018', '20:00'),
    ('sea kale', 'sea food', 'pokazalas ne vkusnoy', 'rybatskoe', '48', '2', '10.01.2018', '21:00'),
    ('wine', 'alcohol', 'otdam 2 butylki krasnogo', 'devyatkino', '1', '6', '02.02.2018', '18:00'),
    ('provencal herbs', 'spice', 'klevye travy, no ne na moy vkus', 'petrogradskaya', '25', '22', '16.10.2018', '14:00'),
    ('pumpkin seeds', 'nuts and seeds', 'ya takoye ne em', 'mejdunarodnaya', '67', '16', '14.11.2018', '19:00'),
    ('semena', 'nuts and seeds', 'godnota dlya popugov', 'lomonosovskaya', '45', '17', '18.11.2018', '14:00'), 
    ('potato soup', 'ready mix', 'ot babushki', 'avtovo', '16', '11','02.09.2018', '14:30'), 
    ('pertushka', 'green', 'iz svoego ogoroda', 'zvenigorodskaya', '63', '10', '11.11.2018', '15:30'), 
    ('izabella', 'wine', 'podarili na prazdnik', 'dostoevskaya', '50', '7', '7.08.2018', '18:30'), 
    ('granatovoye', 'wine', 'ne lublu vino', 'parnas', '19', '6', '14.09.2018', '18:20'), 
    ('water melon', 'fruits and vegetables', 'ochen mnogo na dache', 'devyatkino', '1', '3', '19.08.2018', '10:20'), 
    ('cucumbers', 'fruits and vegetables', 's dachi vezy', 'devyatkino', '1', '9', '19.08.2018', '11:40'), 
    ('choco bins', 'nuts and seeds', 'podarili a u menya allergiya', 'devyatkino', '1', '2', '20.10.2018', '12:00'), 
    ('moloko', 'dairy', 'iz nastoyashi korovy', 'sennaya ploschad', '28', '12', '20.10.2018', '11:00'), 
    ('bulka hleba', 'bread', 'pud hleba razdaet podarki', 'nevsky prospekt', '27', '8', '20.10.2018', '13:30'), 
    ('choco bins', 'nuts and seeds', 'priverly iz kitaya', 'sadovaya', '62', '11', '20.10.2018', '14:00');

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

c.execute('''
INSERT INTO metro_station (station_id, station_name) 
VALUES ('1', 'Devyatkino'), 
('2', 'Grazhdansky Prospekt'), 
('3', 'Akademicheskaya'), 
('4', 'Politekhnicheskaya'), 
('5', 'Ploschad Muzhestva'), 
('6', 'Lesnaya'), 
('7', 'Vyborgskaya'), 
('8', 'Ploshchad Lenina'), 
('9', 'Chernyshevskaya'), 
('10', 'Ploshchad Vosstaniya'), 
('11', 'Vladimirskaya'), 
('12', 'Pushkinskaya'), 
('13', 'Baltiyskaya'), 
('14', 'Narvskaya'), 
('15', 'Kirovsky Zavod'), 
('16', 'Avtovo'), 
('17', 'Leninsky Prospekt'), 
('18', 'Prospekt Veteranov'), 
('19', 'Parnas'), 
('20', 'Prospect Prosvesheniya'), 
('21', 'Ozerki'), 
('22', 'Udelnaya'), 
('23', 'Pionerskaya'), 
('24', 'Chyornaya Rechka'), 
('25', 'Petrogradskaya'), 
('26', 'Gorkovskaya'), 
('27', 'Nevsky Prospekt'), 
('28', 'Sennaya Ploschad'), 
('29', 'Tekhnologichesky Institut '), 
('30', 'Frunzenskaya'), 
('31', 'Moskovskiye Vorota'), 
('32', 'Elektrosila'), 
('33', 'Park Pobedy'), 
('34', 'Moskovskaya'), 
('35', 'Zvyozdnaya'), 
('36', 'Kupchino'), 
('37', 'Begovaya'),
('38', 'Novokrestovskaya'),
('39', 'Primorskaya'), 
('40', 'Vasileostrovskaya'), 
('41', 'Gostiny Dvor'), 
('42', 'Mayakovskaya'), 
('43', 'Ploshchad Alexandra Nevskogo'), 
('44', 'Yelizarovskaya'), 
('45', 'Lomonosovskaya'), 
('46', 'Proletraskaya'), 
('47', 'Obukhovo'), 
('48', 'Rybatskoye'), 
('49', 'Spasskaya'), 
('50', 'Dostoevskaya'), 
('51', 'Ligovsky Prospekt'), 
('52', 'Novocherkasskaya'), 
('53', 'Ladozhskaya'), 
('54', 'Prospekt Bolshevikov'), 
('55', 'Ulitsa Dybenko'), 
('56', 'Komendantskiy Prospekt'), 
('57', 'Staraya Derevnya'), 
('58', 'Krestovsky Island'), 
('59', 'Chkalovskaya'), 
('60', 'Sportivnaya'), 
('61', 'Admiralteyskaya'), 
('62', 'Sadovaya'), 
('63', 'Zvenigorodskaya'), 
('64', 'Obvodny Kanal'), 
('65', 'Volkovskaya'), 
('66', 'Bukharestskaya'), 
('67', 'Mezhdunarodnaya');
''')

conn.commit()

c.execute('''
INSERT INTO users (login)
VALUES
('admin'),
('adaizada'),
('kisa'),
('pupsik'),
('superboy'),
('dasaputeshestvennitza'),
('mitya'),
('vvp'),
('vippersona'),
('prostoychelovek'),
('shkolnik'),
('krokodil'),
('chubayes'),
('nina'),
('tsipa'),
('sportsmen'),
('ucheny'),
('student'),
('passanger'),
('taxomen');
''')


