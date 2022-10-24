from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def redirect_user():
    return redirect('/users/register')

@app.route('/users/register')
def index():
    return render_template('index.html')

@app.post('/users')
def insert_user():
    print(request.form)
    print("hello")
    session['username'] = request.form['username']
    session['location'] = request.form['citylocation']
    session['prog_lang'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/users')

@app.get('/users')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)

