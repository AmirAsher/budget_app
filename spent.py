import sqlite3 as db # included in every python download
from datetime import datetime


def init():
    '''
    initialize a new database to store the expenditure
    '''
    conn = db.connect('spent.db') # create or connect if already exsist
    cur = conn.cursor() # used to execute the sql queries on the db
    sql = '''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER primary key autoincrement,
        amount INTEGER,
        category TEXT,
        message TEXT,
        date TEXT
        )
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()

# init()

def log (amount, category, message='', id=None):
    '''
    logs the expenditure in the database.
    amount: number
    category: string
    message: (optional) string
    '''
    date = str(datetime.now())
    data = (id, amount, category, message, date)
    # conn = sqlite3.connect('spent.db')
    conn = db.connect('spent.db')
    cur = conn.cursor()
    sql = 'INSERT INTO expenses VALUES (?, ?, ?, ?, ?)'
    # sql = '''
    # insert into expenses values (
    #      {},
    #     '{}',
    #     '{}',
    #     '{}'
    #     )
    # '''.format(amount, category, message, date)
    cur.execute(sql, data)
    conn.commit()
    conn.close()


# log(120, "food", "super1")
# log(70, "food", "super2")
# log(100, "home", "arnona")

def view (category=None):
    '''
    returns a list of all expenditure incurred, and the total expense.
    if a category is specified, it only returns info from that category
    '''
    date = str(datetime.now())
    conn = db.connect('spent.db')
    cur = conn.cursor()
    if category:
        sql = '''
        SELECT * FROM expenses WHERE category = '{}'
        '''.format(category)
        sql_sum = '''
        SELECT sum(amount) FROM expenses WHERE category = '{}'
        '''.format(category)
    else:
        sql = '''
        SELECT * FROM expenses
        '''.format(category)
        sql_sum = '''
        SELECT sum(amount) FROM expenses
        '''.format(category)
    cur.execute(sql)
    results = cur.fetchall() # fetch all results that the sql query returns  # will return a list of lists
    cur.execute(sql_sum)
    total_amount = cur.fetchone()[0] # will have only 1 specific value  # return the first elemnt from the list

    return total_amount, results

# print view('food')
# print view()
