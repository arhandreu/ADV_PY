from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(f'Дата: {date.today()}')
    calculate_salary()
    get_employees()

