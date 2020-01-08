from flask import Flask, render_template, request, redirect, url_for
import data_menager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')
@app.route('/question_list/')
def question_data():
    question_data = data_menager.get_data()
    return render_template('question_list.html', question_data = question_data)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )