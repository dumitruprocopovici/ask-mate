from flask import Flask, render_template, request, redirect, url_for
import data_menager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/question_list/', methods=['GET', 'POST'])
def question_data():
    question_data = data_menager.get_data()
    for i in range(len(question_data)):
        question_data[i] = question_data[i][:-1]
    return render_template('question_list.html', question_data = question_data)

@app.route('/question_list/add/', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        title = request.form['Title']
        message = request.form['Message']
        question_data = data_menager.get_data()
        ID = str(int(question_data[-1][0]) + 1)
        Time = 'nothing'
        new_question = []
        new_question.append(ID)
        new_question.append(Time)
        new_question.append(0)
        new_question.append(0)
        new_question.append(title)
        new_question.append(message)
        new_question.append('')
        question_data.append(new_question)
        data_menager.push_data(question_data)
        return redirect('/question_list/')
    return render_template('add_edit_page.html')


@app.route('/question_list/<question_id>')
def display_question(question_id):
    question_data = data_menager.get_data()
    for i in question_data:
        if i[0] == question_id:
            question = i
            break
    return render_template('question_page.html', question = question)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )