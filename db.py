users = {
    'darya': {
        'name': 'Darya Denisova',
        'job_title': 'student',
        'place': 'HSE'
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