from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key = 'secrethush'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

#ninja level 1
@app.route('/add2', methods=['POST'])
def add2():
    session['counter'] += 1 #originally had '+= 2' but incremented the counter by 3 bc it counted the redirect.
    return redirect('/')

#ninja level 2
@app.route('/clear', methods=['POST'])
def clear():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
        
