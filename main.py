import application.salary
import application.db.people
from datetime import date


if __name__ == '__main__':
    print(application.salary.calculate_salary(1000))
    print(date.today())
    print(application.db.people.get_employees())
    print(date.today())
