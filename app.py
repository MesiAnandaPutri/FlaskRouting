from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Success route
#Route ini menampilkan pesan sukses dengan nama pengguna yang dimasukkan.
@app.route('/success/<name>')
def success(name):
    return f'<h1>Halo {name}! Gimana kabarnya hari ini? 😊</h1>'

# Login route
# Memproses data formulir yang dikirimkan dan Menampilkan formulir login melalui login.html.
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # Fetch 'nm' from form
        if user:
            return redirect(url_for('success', name=user))
        else:
            return "Name not provided in form data!", 400
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)