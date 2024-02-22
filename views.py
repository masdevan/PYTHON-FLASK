from flask import Blueprint, render_template, request, jsonify, redirect, url_for  # Tambahkan 'jsonify'

views = Blueprint('views', __name__)

@views.route('/')
def home2():
    return render_template('index.html', name="Devan", age=21)

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/json')
def get_json():  # Hapus titik setelah 'def'
    return jsonify({'name': 'Devan', 'age': 21})  # Perbaiki penulisan 'jsonify'

@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

@views.route('/go-to-home')
def go_to_home():
    args = request.args
    name = args.get('name')
    return redirect(url_for('views.home2'))  # Perbaiki penulisan 'redirect' dan 'url_for'