from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')

    id_matched=[]
    name_matched=[]
    age_matched=[]
    occupation_matched=[]

    for user in USERS:
        if id and user['id'] == id:
            id_matched.append(user)
        if name and name.lower() in user['name'].lower():
            name_matched.append(user)
        if age and (int(age) - 1 <= user['age']<=int(age)+1):
            age_matched.append(user)
        if occupation and occupation.lower() in user['occupation'].lower():
            occupation_matched.append(user)

    all_matched = list ({user['id']: user for user in (id_matched+name_matched+age_matched+occupation_matched)}.values()) #concatinate all user data but with no duplicated

    all_matched.sort(key=lambda user :(
        user in id_matched,
        user in name_matched,
        user in age_matched,
        user in occupation_matched
    ), reverse=True)#sort the values based on the prioroty of search parameters
    return all_matched
