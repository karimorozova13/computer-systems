import sqlite3

def execute_query(sql):
    with sqlite3.connect('salary.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql_avg_paymnet = """
SELECT ROUND(AVG(p.total), 2), e.post
FROM payments as p
LEFT JOIN employees as e ON p.employee_id = e.id
GROUP BY e.post;
"""
sql_employee_by_company = """
SELECT COUNT(*), c.company_name
FROM employees as e
LEFT JOIN companies as c ON e.company_id = c.id
GROUP BY c.id;
"""
sql_by_payment = """
SELECT c.company_name, e.employee, e.post, p.total
FROM companies as c
LEFT JOIN employees e ON e.company_id = c.id
LEFT JOIN payments p ON p.employee_id = e.id
WHERE p.total > 5000
AND p.date_at BETWEEN '2023-07-10' AND '2023-07-20'
"""

print(execute_query(sql_avg_paymnet))
print(execute_query(sql_employee_by_company))
print(execute_query(sql_by_payment))

