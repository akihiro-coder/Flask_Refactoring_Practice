from flask_login import UserMixin, login_manager
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
        return self.password

    def check_password(self, password):
        return check_password_hash(self.password, password)



# ユーザー読み込み
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
