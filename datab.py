c.execute ('''
    INSERT INTO offer (offer_id, name, category, description, location, giver_id, taker_id, time of the deal)
    VALUES ('1', 'chocolate', 'sweet', 'ostalos mnogo shokolada s novogo goda', 'nevsky prospekt', '10', '4', '15/01, 19:00'),
    ('2', 'tomatoes amd cucumbers', 'vegetable', 'svoi ovoschi s gryadki', 'kupchino', '5', '8', '08/08, 12:00'),
    ('3', 'apples', 'fruit', 'narvali u sosedeq, ochen vkusnye', 'prospekt veteranov', '12', '20', '17/09, 10:00'),
    ('4', 'bulochki', 'bread', 'darim schastiye i svejie bulochki v vash dom', 'pekarnya volcheka', '2', '13', '12/12, 23:00'),
    ('5', 'porridge', 'croup', 'navarila kashi na ves rayon', 'kanal griboedova', '1', '7', '21/12, 11:00'),
    ('6', 'zubatka', 'fish', 'zapaha vrode net', 'metro zvezdnaya', '11', '14', '11/12, 20:00'),
    ('7', 'sea kale', 'sea food', 'pokazalas ne vkusnoy', 'rybatskoe', '2', '9', '10/01, 21:00'),
    ('8', 'wine', 'alcohol', 'otdam 2 butylki krasnogo', 'devyatkino', '6', '3', '02/02, 18:00'),
    ('9', 'provencal herbs', 'spice', 'klevye travy, no ne na moy vkus', 'petrogradskiy district', '22', '21', '16/10, 14:00'),
    ('10', 'pumpkin seeds', 'nuts and seeds', 'ya takoye ne em', 'ulitsa belgradskaya', '16', '19', '14/11, 19:00');

''')

offer = {}
offer['offer_id'] = request.form.get('offer_id')
offer['name'] = request.form.get('name')
offer['category'] = request.form.get('category')
offer['description'] = request.form.get('description')
offer['location'] = request.form.get('location')
offer['giver_id'] = request.form.get('giver_id')
offer['date'] = request.form.get('date')
offer['time'] = request.form.get('time')