import sqlite3

def create_db():
    with open('./module5/work_sql/salary.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('salary.db') as conn:
        cur = conn.cursor()
        cur.executescript(sql)

if __name__ =="__main__":
    create_db()