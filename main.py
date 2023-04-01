from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import vk_api


if __name__ == '__main__':
    print('Модуль main.py')
    calculate_salary()
    get_employees()
    print('Текущие дата и время:', datetime.datetime.now())