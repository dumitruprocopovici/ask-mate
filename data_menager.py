import connection

def get_data():
    return connection.read_question()


def push_data(matrix_of_questions):
    return connection.write_question(matrix_of_questions)