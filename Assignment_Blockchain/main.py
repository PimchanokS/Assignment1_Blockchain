from flask import Flask 
from flask import render_template
from flask import request 

from Block import write_block, check_integrity,show_data


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        T1 = request.form.get('T1')
        T2 = request.form.get('T2')
        About = request.form.get('About')
        
        write_block(T1 = T1, T2 = T2, About = About)
    return render_template('index.html')

@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('index.html', checking_results=results)

@app.route('/show')
def show_db():
    data = show_data()
    return render_template('index.html', show=data)

if __name__ == '__main__':
    app.run(debug=True)