from flask import Flask, render_template, url_for, request
from flask.helpers import flash
 
app = Flask(__name__)
app.config['SECRET_KEY']='knjbibib5t2v9o2y0a3m1a4t6b2s6h7l6u5x8a'

color = ['green','blue','red','pink','gray','orange', 'yellow', 'black', 'purple', 'brown']




@app.route("/seminar1")
def index():
    return render_template('index.html', color=color, title='seminar1')

@app.route("/questionnaire", methods=["POST",'GET'])
def anketa():
    if request.method == "POST":
        print (request.form)
        if len(request.form)>2:
            flash('Ваша форма отправлена')
        else:
            flash('Заполните форму полностью')
    return render_template('anketa.html', title='questionnaire' )


@app.route('/about')
def about():
    return render_template('developers.html', title='about' )

@app.route('/Seminars')
def seminars():
    return render_template('Seminars.html', title='Seminars' )


@app.route('/developers')
def developers():
    return render_template('developers.html', title='developers' )


@app.route("/first_page", methods=["POST",'GET'])
def first_page():
    if request.method == "POST":
        print(1)
        print (request.form)
        if len(request.form)>2:
            flash('Your form has been sent')
        else:
            flash('Заполните форму полностью')
    return render_template('first_page.html', title='main page')

if __name__ == "__main__":
   app.run(debug=True)

