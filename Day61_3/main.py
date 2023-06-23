from flask import Flask, render_template
from flakswtfforms import BasicForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.secret_key = 'abcdfg'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    form1 = BasicForm()
    print(f'{form1.email.data},{form1.password.data}')
    if form1.validate_on_submit():
        if form1.email.data == 'ozerutku13@gmail.com' and form1.password.data == 'U147613d':
            return render_template('success.html')
        else :
            return render_template('denied.html')
    #yukaridaki if request.method == 'POST': kullandik.
        
    return render_template('login.html', form = form1)

@app.route('/register1', methods=['POST','GET'])
def register1():
    form = BasicForm()
    if form.validate_on_submit():
        print(f'{form.email.data}{form.password.data}')
    return render_template('login1.html', form = form ) 


if __name__ == '__main__':
    app.run(debug=True)