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
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'})

    return jsonify({'error': 'Invalid input'}), 400


# ログインAPI
@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return jsonify({'message': 'Login successful'})

    return jsonify({'error': 'Invalid credentials'}), 400


# ログアウトAPI
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# ユーザー一覧API
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username} for user in users])


# メインページ
@app.route('/')
def index():
    return render_template('index.html')
