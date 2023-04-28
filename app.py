from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
#    return "<p>Hello, World!</p>"
     return render_template('home.html')

@app.route('/inspect')
def inspect():
    return render_template('inspektai.py')

if __name__ =="__main__":
    app.run(debug=True)