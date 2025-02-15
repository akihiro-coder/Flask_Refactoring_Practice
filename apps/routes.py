from flask import jsonify, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required

from apps import app, db, bcrypt
from apps.forms import LoginForm, RegisterForm
from apps.models import User


# ユーザー登録API
@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if not User.is_duplicate(username):
            User.register(username, password)
            return jsonify({'message': 'User registered successfully'})

    return jsonify({'error': 'Invalid input'}), 400


# ログインAPI
@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        User.login(username, password)

    return jsonify({'error': 'Invalid username or password.'}), 400


# ログアウトAPI
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# ユーザー一覧API
@app.route('/users', methods=['GET'])
def get_users():
    users = db.paginate(User.query.all(), per_page=10)
    return jsonify([{'username': user.username} for user in users])


# メインページ
@app.route('/')
def index():
    return render_template('index.html')
