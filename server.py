from flask import Flask, render_template, request, redirect, url_for
import data_menager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/question_list/')
def question_data():
    question_data = data_menager.get_data()
    for i in range(len(question_data)):
        question_data[i] = question_data[i][:-1]
    return render_template('question_list.html', question_data = question_data)
@app.route('/question_list/add')
def add_question():
    return render_template('add_edit_page.html')

@app.route('/question_list/<question_id>')
def display_question(question_id):
    return render_template('question_page.html', question_id = question_id)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )