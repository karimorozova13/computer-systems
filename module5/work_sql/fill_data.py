from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_COMPANIES = 3
NUMBER_EMPLOYEES = 30
NUMBER_POST = 5

def generate_fake_data(number_companies, number_employees, number_posts):
    fake_companies = []
    fake_employees = []
    fake_posts = []
    
    fake_data = faker.Faker()
    
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())
    
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())
    
    for _ in range(number_posts):
        fake_posts.append(fake_data.job())
    
    return fake_companies, fake_employees, fake_posts

def prepare_data(companies, employees, posts):
    for_companies = []
    for_employees = []
    for_payments = []
    
    for company in companies:
        for_companies.append((company,))
    
    for employee in employees:
        for_employees.append((employee, choice(posts), randint(1, NUMBER_COMPANIES)))
    
    for month in range(1, 12 + 1):
        payment_date = datetime(2023, month, randint(10, 20)).date()
        
        for emp in range(1, NUMBER_EMPLOYEES + 1):
            for_payments.append((emp, payment_date, randint(1000, 10000)))
    
    return for_companies, for_employees, for_payments

def insert_data_to_db(companies, employees, payments):
    with sqlite3.connect('salary.db') as conn:
        cur = conn.cursor()
        
        sql_companies = "INSERT INTO companies(company_name) VALUES(?)"
        cur.executemany(sql_companies, companies)
        
        sql_employees = "INSERT INTO employees(employee, post, company_id) VALUES(?,?,?)"
        cur.executemany(sql_employees, employees)
        
        sql_payments = "INSERT INTO payments(employee_id, date_at, total) VALUES(?,?,?)"
        cur.executemany(sql_payments, payments)
        
        conn.commit()

if __name__ =="__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POST))
    insert_data_to_db(companies, employees, posts)
