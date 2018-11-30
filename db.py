items = {
    '1': {
        'name': 'bread from bakery',
        'category': 'bread',
        'description': 'otdam hleb 5 kilogram',
        'location': 'vladimirskaya',
        'giver_id': 1
        'taker_id': 5
        'time of the deal': '29/12, 16:00'
    },

    '2': {
        'name': 'cucumbers and tomatoes',
        'category': 'vegetables',
        'description': 'otdam v dobriye ruki svoi ovoschi s gryadki',
        'location': 'kupchino',
        'giver_id': 6
        'taker_id': 3
        'time of the deal': '07/10, 12:00'
    },
    '3': {
        'name': 'chocolate',
        'category': 'sweet',
        'description': 'ostalos mnogo shokolada s novogo goda',
        'location': 'nevsky prospekt',
        'giver_id': 10
        'taker_id': 4
        'time of the deal': '15/01, 19:00'
    },

    '4': {
        'name': 'pork',
        'category': 'meat',
        'description': 'ubili sviniyu, sami uje naelis, otdaem svejee myaso',
        'location': 'devyatkino',
        'giver_id': 15
        'taker_id': 88/
        'time of the deal': '13/06, 09:00'
    }
}





_users_list = list(_users.values())


_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)





#get users filtered by name
def get_users_by_name(q):
    results =[]
    # SEARCH

    for user in _user_list:
        if user['name'].lower().find(q.lower()) >=0:
            results.append(user)

    return results



def get_users(username)
    return _users.get(username)
