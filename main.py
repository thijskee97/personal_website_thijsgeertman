from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'





@app.route('/')
def home():
    return render_template('index.html')



@app.route('/p1')
def projects():
    return render_template('p1.html')

@app.route('/p2')
def projects2():
    return render_template('p2.html')

@app.route('/p3')
def projects3():
    return render_template('p3.html')

@app.route('/h4')
def projects4():
    return render_template('h4.html')


if __name__ == "__main__":
    app.run(debug=True)
