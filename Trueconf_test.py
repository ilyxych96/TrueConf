from flask import Flask, jsonify, abort, make_response, request
import json

app = Flask(__name__)

readusers = 'users.json'


def read_json(filename='users.json'):
    with open(filename) as f:
        users = json.load(f)['users']
        return users


def write_json(users, filename='users.json'):
    f = open(filename, 'w', encoding='utf-8')
    f.write('{ "users":')
    json.dump(users, f)
    f.write('}')
    f.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'User not found'}), 404)


@app.route('/', methods=['GET'])
def get_users():
    users = read_json(readusers)
    return jsonify({'users': users})


@app.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    users = read_json(readusers)
    for user in users:
        if user['id'] == user_id:
            return jsonify({'user': user})
    abort(404)


@app.route('/', methods=['POST'])
def create_user():
    users = read_json(readusers)
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': str(int(users[-1]['id']) + 1),
        'name': request.json['name'],
        'sex': request.json.get('sex', ""),
    }
    users.append(user)
    write_json(users)
    return jsonify({'users': users})


@app.route('/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    users = read_json(readusers)
    for user in users:
        if user['id'] == user_id:


            user['name'] = request.json.get('name', user['name'])
            user['sex'] = request.json.get('sex', user['sex'])
            write_json(users)
            return jsonify({'users': users})


@app.route('/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = read_json(readusers)
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            write_json(users)
            return jsonify({'users': users})


if __name__ == '__main__':
    app.run(debug=True)
