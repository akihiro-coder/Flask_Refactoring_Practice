from xmlrpc.client import INTERNAL_ERROR

from flask import jsonify
from flask_login import UserMixin, login_manager, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from apps import db


# ユーザーモデル
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def register(username, password):
        try:
            new_user = User(username=username)
            new_user.hash_password(password)
            db.session.add(new_user)
            db.session.commit()
        except Exception as ex:
            return jsonify({'error': 'Internal error occurred.'}), 500


    @staticmethod
    def is_duplicate(username):
        user = User.query.filter_by(username=username).first()
        if user:
            return True
        else:
            return False

    @staticmethod
    def login(username, password):
        try:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return jsonify({'message': 'Login successfully.'})
        except Exception as ex:
            return jsonify({'error': 'Internal error occurred.'}), 500



# ユーザー読み込み
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
