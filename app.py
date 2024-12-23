from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Success route
#Route ini menampilkan pesan sukses dengan nama pengguna yang dimasukkan.
@app.route('/success/<name>')
def success(name):
    return f'<h1>Halo {name}! Gimana kabarnya hari ini? 😊</h1>'
