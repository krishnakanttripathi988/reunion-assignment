from flask import Flask, jsonify, request
from service.user_service import UserService
from utils.helper import Authentication
from service.database_service import DatabaseService

app = Flask(__name__)
"""
Our database have this much dummy data you can try for:

# USER:
# POSTS:
"""
user = DatabaseService.get_user()
authenticator = Authentication(user)


@app.route('/api/authenticate', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        return jsonify({'token': UserService.getUserAuthenticated(data.get("email_id"),data.get("password"))})
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


@app.route('/api/follow/<id>', methods=['POST'])
@authenticator
def follow_user(authenticated_uid, id):
    try:
        return jsonify({"id":id})
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


# Follow/Unfollow User
@app.route('/api/unfollow/<id>', methods=['POST'])
@authenticator
def unfollow_user(authenticated_uid, id):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


@app.route('/api/user', methods=['GET'])
@authenticator
def get_user_profile(authenticated_uid):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


@app.route('/api/posts', methods=['POST'])
@authenticator
def upload_post(authenticated_uid):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


@app.route('/api/posts/<id>', methods=['DELETE'])
@authenticator
def post_operation(authenticated_uid, id):
    try:
        if request.method == 'DELETE':
            print("hello")
        elif request.method == 'GET':
            print("WORLD")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


# Like/Unlike Post
@app.route('/api/like/<id>', methods=['POST'])
@authenticator
def like_post(authenticated_uid, id):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


# Comment on Post
@app.route('/api/unlike/<id>', methods=['POST'])
@authenticator
def unlike_post(authenticated_uid, id):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


# Unlike a Liked Post
@app.route('/api/comment/<id>', methods=['POST'])
@authenticator
def comment_post(authenticated_uid, id):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500
    

    

@app.route('/api/all_posts', methods=['GET'])
@authenticator
def get_all_post(authenticated_uid, post_id):
    try:
        print("hello")
    except Exception as e:
        return jsonify({'error': 'System Error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
