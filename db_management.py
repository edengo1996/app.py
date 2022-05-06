import sqlite3


def new_user_creation(username_text, pass_text):
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    params = (username_text, pass_text)
    curs.execute("INSERT INTO users VALUES (NULL, ?, ?)", params)
    conn.commit()
    conn.close()
    return True


def is_username_taken(str_input):
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM users WHERE Username = ?', (str_input,)).fetchall()
    if len(curs.fetchall()) == 0:
        return True
    return False


def does_user_exist(str_username, str_pass):
    conn = sqlite3.connect('data_base.db')
    curs = conn.cursor()
    curs.execute('''SELECT * FROM users WHERE Username = ? AND Password = ?;''',
                 (str_username, str_pass))
    if len(curs.fetchall()) == 0:
        return False
    return True

